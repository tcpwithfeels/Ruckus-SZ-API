"""
Author: Justin Francisco
Date Written: 29/03/2023
Last Modified By: Justin Francisco

Description: @TCPwithFeels
Script to read, write or do anything with spreadsheets/csv
Dependencies: openpyxl
"""

import openpyxl

def get_list_mac_hosts(self, SPREADSHEET):
        # Load the Spreadsheet

        wb = openpyxl.load_workbook(SPREADSHEET)

        ############################
        ws = wb["<VALUE>"]
        ############################

        max_row = ws.max_row + 1
        mac_hostname_waplist = []

        # Return list of dictionaries
        for iteration in range(2,max_row):
        
                DICT = {
                    "name" : ws["A{}".format(iteration)].value,
                    "mac"  : ws["B{}".format(iteration)].value,
                    "zoneId": "self.zone_id",
                    "apGroupId": "self.group_id"
                    "model": "Ruckus R510"
                }
                mac_hostname_waplist.append(DICT)

        return mac_hostname_waplist