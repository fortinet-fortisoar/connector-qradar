import requests
import json
from CSConfiguration import CSConfiguration
from qpylib import qpylib
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class CyOPs(object):
    def __init__(self, config):
        self.config = config
        csconfig = CSConfiguration()
        try:
            csconfig.read_configuration()
            self.url = csconfig.config.get('cyops_url')
            self.user = csconfig.config.get('username')
            self.password = csconfig.config.get('password')
            qpylib.log("configuration read" + self.url + " " + self.user + " " + self.password)
        except:
            qpylib.log("Exception while reading config: " + str(sys.exc_info()[0]))

    def getToken(self, username, password):
        endpoint = 'https://' + self.url + '/auth/authenticate'
        qpylib.log('fetching token from endpoint: ' + endpoint)
        data = {'credentials': {'loginid': self.user, 'password': self.password, 'token': ''}}
        ret = requests.post(endpoint, data=json.dumps(data), headers={'Content-Type': 'application/json'}, verify=False)
        resp = ret.json()
        return resp['token']

    def send_offense_id(self, offense_id):
        payload_dict = {"Offense_ID": str(offense_id)}
        qpylib.log("Send offense ID " + str(offense_id))
        if (self.url == '') or (self.user == '') or (self.password == ''):
            return 'Configure the CyberSponse Server details before forwarding the offense data.'
        uri = 'https://' + self.url + '/api/triggers/1/qradar'
        qpylib.log('URI: ' + uri)
        token = self.getToken(self.user, self.password)
        token = json.dumps(token)
        # print(token)
        headers = {"Authorization": "Bearer " + token + ""}
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(uri, verify=False, json=payload_dict, headers=headers)

        if not response.ok:
            raise Exception(
                'Received non-OK response code {} with content {}'.format(response.status_code, response.content))

        else:
            return 'Offense details sent to ' + uri
