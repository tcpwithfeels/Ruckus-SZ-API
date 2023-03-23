"""
Author: Justin Francisco
Date Written: 23/03/2023
Last Modified By: Justin Francisco

Date Last Modified: YYYY/MM/DD
Date Last Tested: YYYY/MM/DD

Result: Pass / Fail

Description: Interaction with Ruckus SZ 100 API to Mass Add Ruckus 510 WAPs
Dependencies: requests json
Usage: `python3 ruckus_AP_add.py`

<description>

"""

import requests
import json
import cprint

class ruckus_SZ_API:

    def __init__(self, host: str):

        self.prefix_pattern = "https://{}:8443/wsg/api/public".format(host)

        self.required_headers = {
            "Content-Type":  "application/json;charset=UTF-8"
        }

    def retrieve_api_version(self):

        # Get the API Version
        
        url = "{}/apiInfo".format(self.prefix_pattern)
        api_version = requests.get(url)

        return api_version
    
    def service_ticket_logon(self, api_version, username, password):
        
        pass

    def ruckus_login(self, api_version, username, password):

        url = "{}/{}/serviceTicket".format(self.prefix_pattern, api_version)

        # Request Body in POST
        # Required [username, password]

        request_body = {
            "username": username,
            "password": password
        }

        try:
            r = requests.post(request_body, data=request_body, verify=verify)
        except requests.exceptions.ConnectionError as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()

        return session
    
    def retrieve_zone_id(self, session, zone_name):
        url = ""
        return zone_id

    def retrieve_group_id(self, session, zone_id, group_name):

        return group_id

    def create_ruckus_ap(self, name, mac, zone_id, group_id):
    # "required" : [ "mac", "zoneId" ]
        return status_code

def main():
    # Main HOST Variable for API Call
    host = "192.X.X.X"
    
    # Ruckus Session 
    ruckus_sesh = ruckus_SZ_API(host)

    # API Version needed for log on
    api_version = ruckus_sesh.retrieve_api_version()

    # 
    ruckus_login(host, api_version, username, password)


if __name__ == '__main__':
    main()

