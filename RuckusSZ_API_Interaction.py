"""
Author: Justin Francisco
Date Written: 23/03/2023
Last Modified By: Justin Francisco

Date Last Modified: YYYY/MM/DD
Date Last Tested: YYYY/MM/DD

Result: Pass / Fail

Description: Interaction with Ruckus SZ 100 API to Mass Add Ruckus 510 WAPs
Dependencies: requests json
Usage: `python RuckusSZ_API_Interaction.py`

"""

import requests
import json

import cprint
import jchecker
import jspreadsheet

from getpass import getpass

"""
API Documentation
https://docs.ruckuswireless.com/smartzone/6.0.0/sz100-public-api-reference-guide-600.html
"""
    
class ruckus_SZ_API:
    # 27/03/2023
    def __init__(self, host: str):
        self.prefix_pattern = "https://{}:8443/wsg/api/public".format(host)

    def retrieve_api_version(self):

        # Get the API Version
        # This will be included in most requests in the URL portion

        url = "{}/apiInfo".format(self.prefix_pattern)
        self.api_version = requests.get(url)
        return self.api_version
    
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
            r = requests.post(request_body, data=request_body, verify=False)
        except requests.exceptions.ConnectionError as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()
        
        self.required_headers = {
            "Content-Type":  "application/json;charset=UTF-8",
            "serviceTicket": r["serviceTicket"]
        }

    # -----------------------
    # Session ID - Logon
    # -----------------------

    def session_id_logon(self, username, password):
        # DEPRICATED unless you're using old API Version
        # Ruckus Logon
        # Use this API command to log on to the controller and acquire a valid logon session.

        url = "{}/{}/sessions".format(self.prefix_pattern, self.api_version)

        # Request Body in POST
        # Required [username, password]
        request_body = {
            "username": username,
            "password": password
        }
        self.service_ticket_value = request_body["serviceTicket"]

        try:
            r = requests.post(url, data=request_body, verify=False)
        except requests.exceptions.ConnectionError as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()
   
    # ------------------------------------------
    # Ruckus Wireless AP Zone - Retrieve List
    # Retrieve Zone ID from List
    # ------------------------------------------

    def retrieve_zone_id(self, zone_name):

        url = "{}/{}/rkszones".format(self.prefix_pattern, self.api_version)
        self.zone_name = zone_name

        """
        {
            "totalCount": 2,
            "hasMore": false,
            "firstIndex": 0,
            "list": [
                {
                "id": "zoneUUID",
                "name": "zoneName"
                },
                {
                "id": "zoneUUID2",
                "name": "zoneName2"
                }
            ]
        }
        """

        r = requests.get(url, headers=self.required_headers, verify=False)
        list_of_zones = r["list"]
        print("List of Zones Here:\n{}".format(list_of_zones))
        for zones in list_of_zones:
            if zones["name"] == zone_name:
                self.zone_id = zones["id"]
                print("""
                ZONE Name {} FOUND\nID Found: {}
                """.format(zone_name, self.zone_id)
                )

    # ------------------------------------------
    # AP Group - Retrieve List
    # Retrieve Group ID from List
    # ------------------------------------------

    def retrieve_group_id(self, group_name):

        url = "{}/{}/rkszones/{}/apgroups".format(self.prefix_pattern, self.api_version, self.zone_id)
        self.group_name = group_name

        """
        {
            "totalCount": 2,
            "hasMore": false,
            "firstIndex": 0,
            "list": [
                {
                "id": "apGroupUUID",
                "name": "apGroupName"
                },
                {
                "id": "apGroupUUID2",
                "name": "apGroupName2"
                }
            ]   
        }
        """

        r = requests.get(url, headers=self.required_headers, verify=False)
        list_of_groups = r["list"]
        print("List of Groups Here:\n{}".format(list_of_groups))
        for groups in list_of_groups:
            if groups["name"] == group_name:
                self.group_id = groups["id"]
                print("""
                Group Name {} FOUND\nID Found: {}
                """.format(group_name, self.group_id)
                )

    # ------------------------------------------
    # AP Group - Create WAP
    # CREATE AP - Specify MAC, Zone and Group
    # ------------------------------------------

    def create_ruckus_ap(self, host_name, mac):
        # "required" : [ "mac", "zoneId" ]
        url = "{}/{}/aps".format(self.prefix_pattern, self.api_version)

        if jchecker.check_ruckus_mac(mac) and jchecker.host_name_checker(host_name):
            
            AP_Info = {
                "mac": mac,
                "zoneId": self.zone_id,
                "apGroupId": self.group_id,
                #"model": "Ruckus R510",
                "name": host_name
            }

            r = requests.post(url, data=AP_Info, headers=self.required_headers, verify=False)

        return r.status_code
    
    # ------------------------------------------
    # AP Verification - Validate WAP
    # Verify AP - DISPLAY
    # ------------------------------------------

    def verify_ruckus_ap(self, mac):
        # "required" : [ "mac", "zoneId" ]
        url = "{}/{}/aps/{}".format(self.prefix_pattern, self.api_version, mac)

        r = requests.post(url, headers=self.required_headers, verify=False)
        json_to_dictionary = json.dumps(r)
        ap_config_dictionary = {
            "name" : json_to_dictionary["apName"],
            "zoneId" : json_to_dictionary["zoneId"],
            "apGroupId" : json_to_dictionary["apGroupId"],
            "model" : json_to_dictionary["model"],
            "administrativeState" : json_to_dictionary["administrativeState"],
        }

        return ap_config_dictionary
    
    # ------------------------------------------
    # Disable LAN Ports on WAP
    # Verify Later
    # ------------------------------------------

    def enable_disable_lan_ports(self, mac, enabled = True):
        url = "{}/{}/aps/{}/specific".format(self.prefix_pattern, self.api_version, mac)
        enable_disable_data = { "lanPorts": [] }
        for iteration in range(1,4):
            lan_port_config = { "portName" : "LAN{}".format(iteration), "enabled" : enabled,  "ethPortProfile": { "id" : "{}".format(iteration) } }    
            enable_disable_data["lanPorts"].append(lan_port_config)

        r = requests.put(url, data = enable_disable_data, headers = self.required_headers, verify=False)
        
        return r.headers

    """
        "lanPorts": [
        {
        "portName": "LAN3",
        "enabled": true,
        "ethPortProfile": {
            "id": "1"
        },
        "overwriteVlanEnabled": true,
        "vlanUntagId": 1,
        "members": "1"
        }
    """

def main():
    #   print(check_ruckus_mac("34159307F00"))
    #   host_name_checker("B98-L6A-R54")
    #   exit()

    # Main HOST Variable for API Call
    # SmartZone 6.0
    host = "131.236.127"
    # Ruckus Session 
    ruckus_sesh = ruckus_SZ_API(host)

    # API Version needed for log on
    api_version = ruckus_sesh.retrieve_api_version()
    print("API Version: {}".format(ruckus_sesh.api_version))
    exit()

    # Generate username and password
    username = input("Username:\n")
    password = getpass("Password:\n")

    # Get the Service Ticket to include in all requests
    ruckus_sesh.service_ticket_logon(host, api_version, username, password)
    print("Service Ticket Produced: {}\n".format(ruckus_sesh.required_headers["serviceTicket"]))

    exit()
    # Get ZONE ID when you specify ZONE name
    #zone_name = "Production"
    zone_name = "Default Zone"
    print("Retrieving ZONE ID from the ZONE NAME: {}".format(zone_name))
    ruckus_sesh.retrieve_zone_id(zone_name) 
    print("ZONE ID Retrieved: {}\n".format(ruckus_sesh.zone_id))

    # Get GROUP ID when you specify GROUP name
    group_name = "Group"
    # group_name = default
    # group_name = LIA
    
    print("Retrieving GROUP ID from the GROUP NAME: {}".format(group_name))
    ruckus_sesh.retrieve_group_id(group_name) 
    print("GROUP ID Retrieved: {}\n".format(ruckus_sesh.group_id))

    exit()
    print("Time to ADD WAP/s to SZ Host")
    input("Press ENTER to CONTINUE: [\\n]")
    
    # Retrieve List of MAC Addresses and Hosts
    list_mac_hostnames = jspreadsheet.get_list_mac_hosts("List_WAPs.xlsx")
    
    # Iterate through the list
    for machosts in list_mac_hostnames:
        try:
            print("MAC Address: {}".format(machosts['mac']))
            print("Hostname: {}".format(machosts['name']))
            print("ZONE ID: {}".format(machosts['zoneId']))
            print("GROUP ID: {}".format(machosts['groupId']))
            input("Correct?\nPress ENTER to CONTINUE: [\\n]")
            
            ruckus_sesh.create_ruckus_ap(machosts['name'], machosts['mac'])

            print(
            """
            ------------------
            Creating WAP - {}

            MAC Address : {}
            Zone ID : {}
            Group ID : {}
            ------------------
            """
            )
            verify = ruckus_sesh.verify_ruckus_ap(machosts['mac'])

            print(
            """
            ------------------
            Validating WAP with MAC - {}

            {}
            Name : {}
            Zone ID : {}
            Group ID : {}
            ------------------
            """.format(machosts['mac'],verify["mac"], verify["zoneId"], verify["groupId"])
            )

        except KeyboardInterrupt as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()

if __name__ == '__main__':
    main()

