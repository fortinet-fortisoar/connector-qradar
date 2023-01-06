""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import json
import arrow
from .conn import QradarConnection
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('qradar')


def get_offenses(config, params, *args, **kwargs):
    # address, token, verify_ssl=False, filter_string=None, *args, **kwargs
    logger.debug('getting offenses from qradar')
    filter_string = str(params.get('filter_string', ''))
    if not filter_string or filter_string == '':
        logger.debug('Using default filter string for offenses in the last 5 minutes')
        t = arrow.utcnow()
        start_time = t.replace(minutes=-5)
        filter_string = 'start_time between {!s} and {!s}'.format(start_time.timestamp * 1000, t.timestamp * 1000)

    q = QradarConnection(**config)
    return q.getOffenses(filter_string)


def query_qradar(config, params, *args, **kwargs):
    # (address, token, search_string, verify_ssl=False, *args, **kwargs):
    logger.debug('Querying QRadar for a custom string')
    search_string = params.get('search_string', '')
    if len(search_string) < 3:
        raise ConnectorError('Search String shorter than 3 characters in len')
    logger.debug('Search string: {}'.format(search_string))
    q = QradarConnection(**config)
    return q.arielSearch(search_string)


def get_events_related_to_offense(config, params, *args, **kwargs):
    # address, token, offense_id, start_time, last_updated_time, max_results=100,verify_ssl=False, *args, **kwargs):
    logger.debug('Looking for events related to an offense')
    if not isinstance(params['max_results'], int):
        logger.warning('Defaulting to 100 max results.')
        params['max_results'] = 100

    qradar_connection = QradarConnection(**config)
    return qradar_connection.getEventsRelatedToOffense(params['offense_id'],
                                                       start_time=params['start_time'][:-5].replace('T', ' '),
                                                       end_time=params['last_updated_time'][:-5].replace('T', ' '),
                                                       result_limit=params['max_results'])


def _check_health(config):
    logger.debug('attempting QRadar connection')
    qradar_connection = QradarConnection(**config)
    return qradar_connection.listVersion()


def close_offense(config, params, *args, **kwargs):
    logger.debug('Attempting to close QRadar offense')
    offense_id = params['offense_id']
    offense_close_id = params['offense_close_id']
    closure_note = params.get('closure_note')
    qradar_connection = QradarConnection(**config)
    return qradar_connection.closeOffense(offense_id, offense_close_id, closure_note=closure_note)


def get_closing_reasons(config, params, *args, **kwargs):
    logger.debug('Attempting to retrieve offense close reasons IDs')
    qradar_connection = QradarConnection(**config)
    return qradar_connection.get_closing_reasons()


def get_offense_type(config, params, *args, **kwargs):
    logger.debug('Attempting to retrieve offense type IDs')
    qradar_connection = QradarConnection(**config)
    return qradar_connection.get_offense_type()


def get_source_ip(config, params, *args, **kwargs):
    ips = params['source_address_ids']
    qradar_connection = QradarConnection(**config)
    return qradar_connection.getSourceIpAddresses(ips)


def get_destination_ip(config, params, *args, **kwargs):
    ips = params['destination_address_ids']
    qradar_connection = QradarConnection(**config)
    return qradar_connection.getDestinationIPAddresses(ips)


def invoke_qradar_api(config, params, *args, **kwargs):
    method = params['method']
    endpoint = params['endpoint']
    request_parameters = params.get('request_parameters', {}) if params.get('request_parameters', {}) else {}
    request_payload = params.get('request_payload') if params.get('request_payload', {}) else {}
    headers = params.get('headers') if params.get('headers', {}) else {}
    qradar_connection = QradarConnection(**config)
    return qradar_connection.invokeQRadarAPI(method, endpoint, request_parameters, headers, json.dumps(request_payload))


def handle_reference_set_value(config, params, *args, **kwargs):
    qradar_connection = QradarConnection(**config)
    method_name = params['method']
    params_value = params.get('value', '')

    reference_set_map = {
        'Retrieves Value': ['get', 'reference_data/sets/{name}'.format(name=params['name'])],
        'Add Value': ['post', 'reference_data/sets/{name}'.format(name=params['name'])],
        'Delete Value': ['delete', 'reference_data/sets/{name}/{value}'.format(name=params['name'], value=params_value)]
    }
    method = reference_set_map[method_name][0]
    endpoint = reference_set_map[method_name][1]
    del params['method']
    response = qradar_connection.invokeQRadarAPI(method, endpoint, params, {})
    response['message'] = 'Successfully perform {0} method on reference set {1}'.format(method_name, params['name'])
    return response


def add_notes(config, params, *args, **kwargs):
    logger.debug('Create a note on an offense.')
    offense_id = params['offense_id']
    closure_note = params.get('closure_note')
    qradar_connection = QradarConnection(**config)
    return qradar_connection.addNote(offense_id, closure_note=closure_note)


def get_notes(config, params, *args, **kwargs):
    logger.debug('Get a note on an offense.')
    offense_id = params['offense_id']
    qradar_connection = QradarConnection(**config)
    return qradar_connection.getNote(offense_id)


operations = {
    'get_offenses': get_offenses,
    'query_qradar': query_qradar,
    'get_events_related_to_offense': get_events_related_to_offense,
    'get_closing_reasons': get_closing_reasons,
    'close_offense': close_offense,
    'get_source_ip': get_source_ip,
    'get_destination_ip': get_destination_ip,
    'invoke_api': invoke_qradar_api,
    'get_offense_type': get_offense_type,
    'handle_reference_set_value': handle_reference_set_value,
    'add_notes': add_notes,
    'get_notes': get_notes
}
