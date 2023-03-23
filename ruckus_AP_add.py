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
import re
from getpass import getpass

"""
API Documentation
https://docs.ruckuswireless.com/smartzone/6.1.0/sz100-public-api-reference-guide-610.html

Common Request Header
The following parameters are required in the HTTP headers of all API requests.

Parameter:      Content-Type	
Value:          “application/json;charset=UTF-8”

-------

Common Request URI Parameters 
The following parameters are required in the Request URI Parameters of all API requests (except for the logon API).

Parameter:	    ServiceTicket	
Value:          {serviceTicket}

serviceTicket is returned as the following parameter in the response payload of the Service Ticket Logon API.
"""

def check_mac(mac_address):
    if re.match(r"^([0-9a-fA-F]{2}:){5}([0-9a-fA-F][0-9a-fA-F])$",mac_address):
        return True
    else:
        print("You inputted: {} \n This is not a valid MAC Address\n")
        exit()

class ruckus_SZ_API:

    def __init__(self, host: str):

        self.prefix_pattern = "https://{}:8443/wsg/api/public".format(host)

        self.required_headers = {
            "Content-Type":  "application/json;charset=UTF-8"
        }

    def retrieve_api_version(self):

        # Get the API Version
        # This will be included in most requests in the URL portion

        url = "{}/apiInfo".format(self.prefix_pattern)
        self.api_version = requests.get(url)
        return api_version
    
    # -----------------------
    # Service Ticket - Logon
    # -----------------------

    def service_ticket_logon(self, api_version, username, password):

        # Use this API command to log on to the controller and acquire a valid service ticket.

        url = "{}/{}/serviceTicket".format(self.prefix_pattern, self.api_version)
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
        self.service_ticket_value = r["serviceTicket"]
        return self.service_ticket_value

    # -----------------------
    # Session ID - Logon
    # -----------------------

    def session_id_logon(self, username, password):
        
        # Ruckus Logon
        # Use this API command to log on to the controller and acquire a valid logon session.

        url = "{}/{}/serviceTicket".format(self.prefix_pattern, self.api_version)

        # Request Body in POST
        # Required [username, password]

        request_body = {
            "username": username,
            "password": password
        }
        request_body["serviceTicket"] = self.service_ticket_value

        try:
            r = requests.post(url, data=request_body, verify=False)
        except requests.exceptions.ConnectionError as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()

        return session
    
    def retrieve_zone_id(self, zone_name):
        url = "{}/{}/rkszones".format(self.prefix_pattern, self.api_version)
        r = requests.get(url, verify=False)
        list_of_zones = r["list"]

        for zones in list_of_zones:
            if zones["name"] == zone_name:
                self.zone_id = zones["id"]

        return self.zone_id

    def retrieve_group_id(self, group_name):

        url = "{}/{}/rkszones/{}/apgroups".format(self.prefix_pattern, self.api_version, self.zone_id)
        r = requests.get(url, verify=False)
        list_of_groups = r["list"]

        for groups in list_of_groups:
            if groups["name"] == group_name:
                self.group_id = groups["id"]
        
        return self.group_id


    """
    {
        "mac": "00:11:22:33:44:55",
        "zoneId": "zoneUUID",
        "apGroupId": "apGroupUUID",
        "serial": "00000096",
        "model": "ZF7962",
        "name": "apName",
        "gpsSource": "MANUAL",
        "latitude": 22.3,
        "longitude": 114,
        "location": "shenzhen",
        "description": "apDescription",
        "administrativeState": "Unlocked",
        "provisionChecklist": "test",
        "bssColoringEnable": true
    }
    """

    def create_ruckus_ap(self, host_name, mac):
        # "required" : [ "mac", "zoneId" ]

        url = "{}/{}/aps".format(self.prefix_pattern, self.api_version)
        AP_Info = {
            "mac": mac,
            "zoneId": self.zone_id,
            "apGroupId": self.group_id,
            "model": "R510",
            "name": host_name
        }

        r = requests.get(url, data=AP_info, verify=False)
        
        return status_code

def main():
    # Main HOST Variable for API Call
    host = "192.X.X.X"
    
    # Ruckus Session 
    ruckus_sesh = ruckus_SZ_API(host)

    # API Version needed for log on
    api_version = ruckus_sesh.retrieve_api_version()

    # Generate username and password
    username = input("Username:\n")
    password = getpass("Password:\n")

    # Get the Service Ticket to include in all requests
    ruckus_sesh.session_ticket_logon(host, api_version, username, password)
    print("Service Ticket Produced: {}\n".format(ruckus_sesh.service_ticket_value))

    
    # Get ZONE ID when you specify ZONE name
    zone_name = "Zone"
    print("Retrieving ZONE ID from the ZONE NAME: {}".format(zone_name))
    ruckus_sesh.retrieve_zone_id(zone_name) 
    print("ZONE ID Retrieved: {}".format(ruckus_sesh.zone_id))

    print("Retrieving AP Group ID")
    # Get GROUP ID when you specify GROUP name
    group_name = "Group"
    print("Retrieving GROUP ID from the GROUP NAME: {}".format(group_name))
    ruckus_sesh.retrieve_group_id(group_name) 
    print("GROUP ID Retrieved: {}".format(ruckus_sesh.group_id))

    



if __name__ == '__main__':
    main()

