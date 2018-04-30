#!/usr/bin/env python
"""ScienceLogic Monitoring Utility.

Disable/Enable monitoring on devices.
"""
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ScienceLogic:

    def __init__(self, uri, user, password, ssl_verify=False):
        """Inits with connection established."""
        self.query_url = uri + '/api/device/'
        self.uri = uri
        self.user = user
        self.upass = password
        self.verify = ssl_verify
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(user, password)

    def disable_monitoring(self, dev_id):
        """
        disable monitoring on the device
        :param dev_id: Device ID in ScienceLogic, uri format
        :return: boolean
        """
        if dev_id is None:
            return False
        dev_url = self.uri + dev_id
        data = {'active': {'user-initiated-maintenance': '1'}}
        payload = json.dumps(data)
        response = self.session.put(dev_url, data=payload, verify=self.verify)
        if response.status_code != 200:
            return False
        else:
            return True

    def enable_monitoring(self, dev_id):
        """
        Enable monitoring on the device
        :param dev_id: Device ID in ScienceLogic, uri format
        :return: boolean
        """
        if dev_id is None:
            return False
        dev_url = self.uri + dev_id

        data = {'active': {'user-initiated-maintenance': '0'}}
        payload = json.dumps(data)
        response = self.session.put(dev_url, data=payload, verify=self.verify)
        if response.status_code != 200:
            return False
        else:
            return True

    def get_id(self, dev_name):
        """
        Retrieve a device's ID from ScienceLogic
        :param dev_name: Device name
        :return: ID, uri format
        """
        query = self.query_url + '?filter.name.in=' + dev_name
        response = self.session.get(query, verify=self.verify)
        if response.status_code != 200:
            return None

        response = response.json()
        if response['total_matched'] == 1:
            return response['result_set'][0]['URI']
        return None


if __name__ == "__main__":
    # print(getID('tus1grcappdin18'))
    sl = ScienceLogic("https://", "em7", "em7")
    print(sl.get_id('TUS1GRCAPPDIN18'))
    # sl.enable_monitoring('CHG0091368', sl.get_id('TUS1GRCAPPDIN18'))
    # enable_monitoring('1')
