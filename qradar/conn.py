""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import requests
from time import sleep
import logging
from connectors.core.connector import ConnectorError

logger = logging.getLogger(__name__)


class QradarConnection(object):
    MAX_ALLOW_SEARCH_SECS = 600

    def __init__(self, address, token, verify_ssl=True, api_version='6.0', **kwargs):
        self.address = address
        if not address.startswith('https://') and not address.startswith('http://'):
            self.address = 'https://{0}'.format(address)
        self.token = token
        self.verify_ssl = verify_ssl
        self.api_version = api_version
        self.base_url = '{}/api'.format(self.address)
        self.log = logger
        self.__genSession()

    def __genSession(self):
        self.log.debug('Creating Session')
        self.session = requests.Session()
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'SEC': self.token,
            'Version': str(self.api_version),
        }
        self.session.headers.update(headers)
        self.session.verify = self.verify_ssl

    def __parseRequestResult(self, results):
        if not results.ok:
            raise ConnectorError('Response from server: {}'.format(str(results.content)))
        self.log.debug('Parsing request return data')
        self.log.debug('Return Status Code: {}'.format(results.status_code))
        self.log.debug('Return Text: {}'.format(results.text))
        if len(results.text) > 0:
            self.log.debug('Returning assumed json.')
            return results.json()
        else:
            self.log.warning('Warning returning empty list... ')
            return []

    def __postUrl(self, endpoint, params={}, headers={}, data={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('POST to URL: {}'.format(url))
        res = self.session.post(url, params=params, headers=headers, data=data)
        return self.__parseRequestResult(res)

    def __patchUrl(self, endpoint, params={}, headers={}, data={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('PATCH to URL: {}'.format(url))
        res = self.session.patch(url, params=params, headers=headers, data=data)
        return self.__parseRequestResult(res)

    def __getUrl(self, endpoint, params={}, headers={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('GET to URL: {}'.format(url))
        res = self.session.get(url, params=params, headers=headers)
        return self.__parseRequestResult(res)

    def __deleteUrl(self, endpoint, params={}, headers={}, data={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('GET to URL: {}'.format(url))
        res = self.session.delete(url, params=params, headers=headers, data=data)
        return self.__parseRequestResult(res)

    def __getArielResults(self, searchId):
        endpoint = 'ariel/searches/{}'.format(searchId)
        totalSearchTime = 0
        while True:
            res = self.__getUrl(endpoint)
            status = res.get('status', '').lower()
            if status == 'completed':
                break
            elif totalSearchTime >= self.MAX_ALLOW_SEARCH_SECS:
                msg = 'Search took longer than {} seconds to complete so we quit trying.'.format(
                    self.MAX_ALLOW_SEARCH_SECS)
                self.log.error(msg)
                raise RuntimeError(msg)
            totalSearchTime += 10
            self.log.debug('Waiting for search results: total search time {}'.format(totalSearchTime))
            sleep(10)
        endpoint = '{}/results'.format(endpoint)
        return self.__getUrl(endpoint)

    def __ensureStr(self, variable):
        if isinstance(variable, str):
            return variable
        elif isinstance(variable, bytes):
            return variable.decode("utf-8")
        else:
            raise TypeError('Cant convert type({}) to string'.format(type(variable)))

    def validateCSAppInstalled(self):
        endpoint = 'config/extension_management/extensions'
        params = {'fields': 'name, version, id'}
        extn_response = self.__getUrl(endpoint, params=params)
        app_installed = False
        for record in extn_response:
            if 'cybersponse' in record['name'].lower():
                app_installed = True
        if not app_installed:
            logger.warning('CyberSponse App is not installed on the QRadar server {}'.format(self.base_url))
        return 'Validated connections. However, CyberSponse App is not installed on the QRadar server'

    def listVersion(self):
        endpoint = 'help/versions'
        response = self.__getUrl(endpoint)
        if response:
            logger.info("Check health successful..")
            return True

    def arielSearch(self, search_string, **kwargs):
        endpoint = 'ariel/searches'
        self.log.debug('Running ariel search')
        search_string = self.__ensureStr(search_string)
        self.log.debug('Search string: {}'.format(search_string))
        params = {
            'query_expression': search_string,
        }
        res = self.__postUrl(endpoint, params=params)
        searchId = res.get('search_id')
        return self.__getArielResults(searchId)

    def getOffenses(self, filter_string, **kwargs):
        # https://www.ibm.com/support/knowledgecenter/SS42VS_7.3.0/com.ibm.qradar.doc/c_rest_api_filtering.html
        # https://www.ibm.com/support/knowledgecenter/SS42VS_7.3.0/com.ibm.qradar.doc/8.0--siem-offenses-GET.html
        endpoint = 'siem/offenses'
        self.log.debug('Getting offenses')
        filter_string = self.__ensureStr(filter_string)
        self.log.debug('Filter String: {}'.format(filter_string))
        params = {
            'filter': filter_string
        }

        res = self.__getUrl(endpoint, params=params)
        return res

    def getEventsRelatedToOffense(self, offense_id, start_time, end_time, result_limit=100, **kwargs):
        self.log.debug('Getting events related to offenseid {}'.format(offense_id))
        searchString = "select * from events where InOffense({}) limit {} start '{}' stop '{}'".format(offense_id,
                                                                                                       result_limit,
                                                                                                       start_time,
                                                                                                       end_time)
        return self.arielSearch(searchString)

    def closeOffense(self, offense_id, offense_close_id, closure_note=None, **kwargs):
        if closure_note:
            self.log.debug("Adding closure note {}".format(closure_note))
            endpoint = "siem/offenses/{}/notes".format(offense_id)
            params = {"note_text": closure_note}
            res = self.__postUrl(endpoint, params=params)

        self.log.debug('Closing offenseid {}'.format(offense_id))
        endpoint = 'siem/offenses/{}'.format(offense_id)
        self.log.debug('Getting offenses')
        params = {"closing_reason_id": offense_close_id, "status": "CLOSED"}
        res = self.__postUrl(endpoint, params=params)
        return res

    def addNote(self, offense_id, closure_note=None, **kwargs):
        self.log.debug("Adding closure note {}".format(closure_note))
        endpoint = "siem/offenses/{}/notes".format(offense_id)
        params = {"note_text": closure_note}
        res = self.__postUrl(endpoint, params=params)
        return res

    def getNote(self, offense_id, **kwargs):
        self.log.debug("Get notes of  {}".format(offense_id))
        endpoint = "siem/offenses/{}/notes".format(offense_id)
        res = self.__getUrl(endpoint)
        return res

    def get_closing_reasons(self):
        self.log.debug('Retrieving offense closing reason IDs')
        endpoint = 'siem/offense_closing_reasons'
        res = self.__getUrl(endpoint)
        return res

    def get_address_details(self, endpoint, ips, params_fields):
        chunk = 100  # limit of send ips to GET request
        result = []
        for i in range(0, len(ips), chunk):
            start = i
            filter_string = 'id in (' + ",".join(map(str, ips[start:start + chunk])) + ')'
            self.log.info('Filter String: {}'.format(filter_string))
            params = {
                'filter': filter_string,
                'fields': params_fields
            }
            res = self.__getUrl(endpoint, params=params)
            result += res
        return result

    def getSourceIpAddresses(self, ips, **kwargs):
        endpoint = 'siem/source_addresses'
        self.log.debug('Getting ip details')
        # TODO: validate ids
        params_fields = 'id, source_ip, network, magnitude'
        result = self.get_address_details(endpoint, ips, params_fields)
        return result

    def getDestinationIPAddresses(self, ips, **kwargs):
        endpoint = 'siem/local_destination_addresses'
        self.log.debug('Getting destination ip details')
        params_fields = 'id, local_destination_ip, network, magnitude'
        # TODO: validate ids
        res = self.get_address_details(endpoint, ips, params_fields)
        return res

    def invokeQRadarAPI(self, method, endpoint, params, headers, data={}):
        endpoint = endpoint.lstrip('/')
        if method.lower() == 'get':
            res = self.__getUrl(endpoint, params=params, headers=headers)
        elif method.lower() == 'post':
            res = self.__postUrl(endpoint, params=params, headers=headers, data=data)
        elif method.lower() == 'patch':
            res = self.__patchUrl(endpoint, params=params, headers=headers, data=data)
        elif method.lower() == 'delete':
            res = self.__deleteUrl(endpoint, params=params, headers=headers, data=data)
        else:
            raise ConnectorError('Unsupported request method')
        return res

    def get_offense_type(self):
        self.log.debug('Retrieving offense type IDs')
        endpoint = 'siem/offense_types'
        res = self.__getUrl(endpoint)
        return res
