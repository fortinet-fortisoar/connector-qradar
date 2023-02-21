""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import requests
import json
from time import sleep
from connectors.core.connector import get_logger, ConnectorError
from requests_toolbelt.utils import dump

logger = get_logger("qradar")


class QradarConnection(object):
    MAX_ALLOW_SEARCH_SECS = 600
    MAX_RESULTS = 100
    endpoints = {
        'get_assets_properties': 'asset_model/properties',
        'get_assets': 'asset_model/assets',
        'update_asset': 'asset_model/assets/{asset_id}',
        'get_cases': 'forensics/case_management/cases',
        'create_case': 'forensics/case_management/cases',
        'get_reference_tables': 'reference_data/tables',
        'get_table_elements': 'reference_data/tables/{name}',
        'add_table_element': 'reference_data/tables/{name}',
        'delete_table_element': 'reference_data/tables/{name}/{outer_key}/{inner_key}',
        'delete_reference_table': 'reference_data/tables/{name}'

    }
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
            if results.status_code in [200, 201, 202, 204]:
                try:
                    json.loads(results.content)
                    self.log.debug('Returning assumed json.')
                    return results.json()
                except ValueError as e:
                    self.log.debug('Returning assumed text.')
                    return results.content
        else:
            self.log.warning('Warning returning empty list... ')
            return []

    def __postUrl(self, endpoint, params={}, headers={}, data={}, json={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('POST to URL: {}'.format(url))
        res = self.session.post(url, params=params, headers=headers, data=data, json=json)
        logger.debug('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:\n{0}\n'.format(dump.dump_all(res).decode('utf-8')))
        return self.__parseRequestResult(res)

    def __patchUrl(self, endpoint, params={}, headers={}, data={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('PATCH to URL: {}'.format(url))
        res = self.session.patch(url, params=params, headers=headers, data=data)
        logger.debug('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:\n{0}\n'.format(dump.dump_all(res).decode('utf-8')))
        return self.__parseRequestResult(res)

    def __getUrl(self, endpoint, params={}, headers={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('GET to URL: {}'.format(url))
        res = self.session.get(url, params=params, headers=headers)
        logger.debug('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:\n{0}\n'.format(dump.dump_all(res).decode('utf-8')))
        return self.__parseRequestResult(res)

    def __deleteUrl(self, endpoint, params={}, headers={}, data={}):
        url = '{}/{}'.format(self.base_url, endpoint)
        self.log.debug('GET to URL: {}'.format(url))
        res = self.session.delete(url, params=params, headers=headers, data=data)
        logger.debug('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:\n{0}\n'.format(dump.dump_all(res).decode('utf-8')))
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
        elif isinstance(variable, dict):
            return json.dumps(variable)
        elif isinstance(variable, bool):
            return str(variable).lower()
        elif isinstance(variable, int):
            return variable
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

#1.6.0
    def __args_parser(self, params):
        """
        Builds url_params, headers and POST payloads from params
        :param params: info.json Params
        :return: url_params, headers, json data ready for requests
        """
        data = {}
        url_params = {}
        headers = {}
        for key, value in params.items():
            if key == 'filter_string' and value:
                url_params.update({"filter": self.__ensureStr(value)})
            elif key == 'max_results':
                max_results = str(value) if value else str(self.MAX_RESULTS)
                headers.update({'Range': 'items=0-' + str(max_results)})
            elif 'body' in key:
                kv_input = key.split('.')
                if isinstance(value, dict):
                    logger.debug('Request JSON data: {}'.format(value))
                    data = value
                    headers.update({'Content-type': 'application/json', 'Accept': params.get('content_type','application/json')})
                else:
                    data.update({kv_input[1]:value})
            elif 'query' in key and value:
                url_params.update({key.split('.')[1]:self.__ensureStr(value)})
        return url_params, headers, data


    def __build_endpoint(self,params):
        """
        Formats endpoint string
        :param endpoint: endpoint string
        :return: formatted endpoint string
        """
        endpoint = self.endpoints[params.get('operation')]
        for key, value in params.items():
            if value is not None and 'path' in key:
                param_name = key.split('.')[1]
                endpoint = endpoint.replace('{' + param_name + '}', str(value))
            elif value is None and 'path' in key:
                raise ConnectorError('Path parameters cannot be null')
        logger.debug('Building endpoint: {}'.format(endpoint))
        return endpoint

    def get_record(self, params):
        """
        Run GET operations
        :param params: info.json Params
        :return: API call response content
        """
        endpoint = self.__build_endpoint(params)
        url_params, headers, data = self.__args_parser(params)
        self.log.debug('Getting Records. \nParams: {0}, \nHeaders: {1}'.format(url_params, headers))
        return self.__getUrl(endpoint, params=url_params, headers=headers)


    def update_record(self, params):
        """
        Run POST operations
        :param params: info.json Params
        :return: API call response content
        """
        endpoint = self.__build_endpoint(params)
        url_params, headers, data = self.__args_parser(params)
        self.log.debug('Updating Record. \nParams: {0} \nHeaders: {1} \nData: {2}'.format(url_params, headers, data))
        return self.__postUrl(endpoint, headers=headers, params=url_params, json=data)


    def delete_record(self, params):
        """
        Run DELETE operations
        :param params: info.json Params
        :return: API call response content
        """
        endpoint = self.__build_endpoint(params)
        url_params, headers, data = self.__args_parser(params)
        self.log.debug('Deleting Record. \nParams: {0} \nHeaders: {1}'.format(url_params, headers))
        return self.__deleteUrl(endpoint, headers=headers, params=url_params)