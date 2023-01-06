""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import Connector
from .funcs import operations, _check_health
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('qradar')


class qradar(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.debug('execute(): Input is %s' % operations.get(operation))
        try:
            operation = operations.get(operation)
        except Exception:
            return ['messagePROBLEM']
        return operation(config, params, **kwargs)

    def check_health(self, config):
        logger.debug('starting health check')
        return _check_health(config)
