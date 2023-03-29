"""
Author: Justin Francisco
Date Written: 29/03/2023
Last Modified By: Justin Francisco

Description: @TCPwithFeels
Script to read, write or do anything with spreadsheets/csv
Dependencies: openpyxl
"""

import openpyxl
from datetime import date

today = date.today()
date_format = today.strftime("%d/%m/%Y")

def get_list_mac_hosts(self, SPREADSHEET, WORKSHEET = "Sheet1"):
    
    # Load the Spreadsheet
    wb = openpyxl.load_workbook(SPREADSHEET)
    ws = wb[WORKSHEET]

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

def scan_to_spready(self, SPREADSHEET, WORKSHEET = "Sheet1"):
    # Load the Spreadsheet
    wb = openpyxl.load_workbook(SPREADSHEET)
    ws = wb[WORKSHEET]

    # Return list of dictionaries
    max_row = ws.max_row + 1
    row_to_start = input("Where in the {} Spreadsheet do you want to start?".format(SPREADSHEET))

    for iterations in range(row_to_start,max_row):
        hostname = ws["A{}".format(iterations)].value
        mac_address = input("MAC Address for {}:".format(hostname))
        print("Writing Mac Address to Spreadsheet at Cell B-{}".format(iterations))
        ws['B{}'.format(iterations)] = str(mac_address)

    wb.save("{}-{}".format(SPREADSHEET, date_format))
    wb.close()

def spready_builder(self, SPREADSHEET, WORKSHEET = "Sheet1"):
    pass
