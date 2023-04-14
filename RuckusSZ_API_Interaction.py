"""
Author: Justin Francisco
Date Written: 23/03/2023
Last Modified By: Justin Francisco

Date Last Modified: 14/04/2023
Date Last Tested: DD/MM/YYYY

Result: Pass / Fail

Description: Interaction with Ruckus SZ 100 API to Mass Add Ruckus 510 WAPs
Dependencies: requests json
Usage: `python RuckusSZ_API_Interaction.py credentials.json`

"""

import requests
import json
import logging
import sys

import cprint
import jchecker
import jspreadsheet

from getpass import getpass

"""
API Documentation
https://docs.ruckuswireless.com/smartzone/6.0.0/sz100-public-api-reference-guide-600.html

"""
    
class ruckus_SZ_API:

    def __init__(self, host=None, api_version="v8_2"):
        
        if host == None:
            print(" - Hostname Needed for API Requests- ")
            host = input("Host: ")
        
        self.prefix_pattern = "https://{}:8443/wsg/api/public/{}/".format(host, api_version)

        self.required_headers = {
            "Content-Type":  "application/json;charset=UTF-8"
        }

    #--------------------------------------------
    # --- Service Ticket - Logon - POST CALL ---
    #--------------------------------------------

    def service_ticket_logon(self, username=None, password=None):

        if username == None:
            print(" - Credentials Needed - ")
            username = input("Username: ")
        if password == None:
            password = getpass("Password: ")
        # Use this API command to log on to the controller and acquire a valid service ticket.
        url = "{}/serviceTicket".format(self.prefix_pattern)

        request_body = {
            "username": username,
            "password": password
        }

        #self.s is the NEW session

        try:
            # Creating new requests session
            self.s = requests.Session()

            # Adding "Content-Type = application/json;charset=UTF-8" to headers in each request
            self.s.headers.update(self.required_headers)

            # r (response) is doing a post request
            r = self.s.post(url, data=request_body, verify=False)

            # turn the response into Python Dictionary from a JSON data
            json_response = r.json()
            
        except requests.exceptions.ConnectionError as e:
            cprint("Unable to establish session to Ruckus Smart Zone:\n  ", 'red', True)
            cprint(e,'yellow')
            exit()

        # Add the service ticket now into each header
        self.s.headers.update( { "serviceTicket": json_response["serviceTicket"] } )
        
        return json_response["serviceTicket"]
   
    #----------------------------------------------------
    # --- Retrieve Zone ID - POST CALL - Output List ---
    #----------------------------------------------------

    def retrieve_zone_id(self, zone_name):

        url = "{}rkszones".format(self.prefix_pattern)

        # r (response) is doing a post request
        r = self.s.get(url, verify=False)
        
        list_of_zones = r["list"]

        print("List of Zones Here:\n{}".format(list_of_zones))

        for zones in list_of_zones:
            if zones["name"] == zone_name:
                self.zone_id = zones["id"]
                print("""
                ZONE Name {} FOUND\nID Found: {}
                """.format(zone_name, self.zone_id)
                )
                break

        return self.zone_id
    
    #------------------------------------------------------
    # --- Retrieve Group ID - POST CALL - Outputs List ---
    #------------------------------------------------------

    def retrieve_group_id(self, group_name):

        url = "{}rkszones/{}/apgroups".format(self.prefix_pattern, self.zone_id)

        # r (response) is doing a post request
        r = self.s.get(url, verify=False)
        
        list_of_groups = r["list"]

        print("List of Zones Here:\n{}".format(list_of_group))

        for groups in list_of_groups:
            if groups["name"] == group_name:
                self.group_id = groups["id"]
                print("""
                GROUP Name {} FOUND\nID Found: {}
                """.format(group_name, self.group_id)
                )
                break

        return self.group_id
    
    # ------------------------------------------
    # AP Group - Create WAP
    # CREATE AP - Specify MAC, Zone and Group
    # ------------------------------------------
    def _verify_ruckus_ap(self, mac_addr=None):
        # DOES AP exist in controller already    
        # /v8_2/aps/{apMac}

        url = "{}aps/mac".format(self.prefix_pattern, mac_addr)
        r = self.s.get(url, verify=False)

        if r.status_code != 200:

            return False
        
        else:
            message = """
#------------------------------------------
# --- AP of MAC >> {} << Exists already ---
#------------------------------------------
            """.format(mac_addr)
            print(message)

            return True

    def create_ruckus_ap(self, host_name=None, mac=None, location=None, description=None):
        
        # /v8_2/aps
        url = "{}aps".format(self.prefix_pattern)

        
        if jchecker.check_ruckus_mac(mac):

            AP_Info = {
                "mac": mac,
                "zoneId": self.zone_id,
                "name": host_name,
                "location": location
            }

            if location != None:
                AP_Info["location"] = location
            if description != None:
                AP_Info["description"] = description

            # VERIFY if AP exists already in controller
            if self._verify_ruckus_ap(mac_addr=mac):
                try:
                    r = self.s.post(url, data=AP_Info, verify=False)

                    if r.status_code == 200:

                        message = """
#----------------------------------------------
# --- AP with MAC >> {} << Has Been Created ---
#----------------------------------------------
                        """.format(mac)

                        print(message)               

                except requests.exceptions.ConnectionError as e:
                    cprint("Unable to add access point\n  ", 'red', True)
                    cprint(e,'yellow')
                
            else:
                pass
    
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

        r = requests.put(url, data=enable_disable_data, headers = self.required_headers, verify=False)
        
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
    if ".json" is not sys.argv[1]:
        f = sys.argv[1] + ".json"
    else:
        f = sys.argv[1]

    try:
        with open(f, "r") as f_js:
            data = json.load(f_js)
            host = data['smartzone_info']['host']
            api_version = data['smartzone_info']['api_version']
            username = data['credz']['username']
            password = data['credz']['password']

    except FileNotFoundError:
        print("The file {} does not exist".format(f))
        print("Credentials File Does Not Exist")
        
    # Main HOST Variable for API Call
    # Ruckus Session 
    ruckus_sesh = ruckus_SZ_API(host)

    # Get the Service Ticket to include in all requests
    serviceTicket = ruckus_sesh.service_ticket_logon(username, password)

    print("Service Ticket Produced: {}\n".format(serviceTicket))

    # Get ZONE ID when you specify ZONE name
    # zone_name = "Default"

    zone_name = "Default Zone"
    print("Retrieving ZONE ID from the ZONE NAME: {}".format(zone_name))
    ruckus_sesh.retrieve_zone_id(zone_name) 
    print("ZONE ID Retrieved: {}\n".format(ruckus_sesh.zone_id))

    # Get GROUP ID when you specify GROUP name
    # May not need this
    
    # -----------------------------------------------------------------------
    # group_name = "default"
    # print("Retrieving GROUP ID from the GROUP NAME: {}".format(group_name))
    # ruckus_sesh.retrieve_group_id(group_name) 
    # print("GROUP ID Retrieved: {}\n".format(ruckus_sesh.group_id))
    # -----------------------------------------------------------------------

    #-------------------------------
    # --- TEST THESE MACS FIRST ---
    #-------------------------------

    ruckus_sesh.create_ruckus_ap(host_name="B50-LGF-RG02", 
                                 mac="341593007EB0", 
                                 location="Room G02, Building 50", 
                                 description="H510 for Building 50 Room G02")
    #exit()

    ruckus_sesh.create_ruckus_ap(host_name="B50-LGF-RG07", 
                                 mac="341593007210", 
                                 location="Room G07, Building 50", 
                                 description="H510 for Building 50 Room G07")
    #exit()

    ruckus_sesh.create_ruckus_ap(host_name="B50-LGF-RG10", 
                                 mac="34159302BE70", 
                                 location="Room G10, Building 50", 
                                 description="H510 for Building 50 Room G10")
    #exit()


    # Retrieve List of MAC Addresses and Hosts
    list_mac_hostnames = jspreadsheet.get_list_mac_hosts(SPREADSHEET="WAP info for SmartZone.xlsx", WORKSHEET="H510")
    
    print(list_mac_hostnames)
    print("""
#--------------------------------------
# --- DOES THIS LIST LOOK CORRECT? ---
#--------------------------------------
"""
          )

    for ite_d in list_mac_hostnames:

        try:
            print()
            print("MAC Address: {}".format(ite_d['mac']))
            print("Hostname: {}".format(ite_d['name']))
            print("ZONE ID: {}".format(ite_d['zoneId']))
            print("Location: {}".format(ite_d['location']))
            print("Description: {}".format(ite_d['description']))
            print()
            input("Correct?\nPress ENTER to CONTINUE: [\\n]")

            ruckus_sesh.create_ruckus_ap(host_name=ite_d['name'], mac=ite_d['mac'], location=ite_d['location'], description=ite_d['description'])
         
        except KeyboardInterrupt as e:
            
            continue
    exit()

if __name__ == '__main__':
    main()

