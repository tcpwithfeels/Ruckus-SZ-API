

def scan_to_spready(self, SPREADSHEET):
    wb = openpyxl.load_workbook(SPREADSHEET)
    ws = wb["Sheet1"]
    # Return list of dictionaries
    max_row = ws.max_row + 1
    mac_hostname_waplist = []
    row_to_start = input("Where in the {} Spreadsheet do you want to start?".format(SPREADSHEET))
    for iterations in range(row_to_start,max_row):
        hostname = ws["A{}".format(iterations)].value
        mac_address = input("MAC Address for {}:".format(hostname))
        print("Writing Mac Address to Spreadsheet at Cell B-{}".format(iterations))
        ws['B{}'.format(iterations)] = str(mac_address)