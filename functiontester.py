import jchecker
import jspreadsheet
import cprint


mac_address = "341593017F00"

#username = "icts_script"
#password = "7\"4TatJ_9[l.<MEM" 
#jchecker.check_ruckus_mac(mac_address)
print(jchecker.check_ruckus_mac("34:15:93:01:7F:00"))
print(jchecker.check_ruckus_mac("34:15:93:01:7F:00"))
print(jchecker.check_ruckus_mac("34:15:93:01:7F:00"))
print(jchecker.check_ruckus_mac("34:15:93:01:7F:00"))
print(jchecker.check_ruckus_mac("34:15:93:01:7F:00"))

cprint.jprint_cmd_banner("34:15:93:01:7F:00")

cprint.jhash_header("FUNCTION CALL WRITTEN HERE", space=True)
cprint.jhash_header("Service Ticket - Logon - POST CALL", space=True)

print(jchecker.create_border("34:15:93:01:7F:00"))


cprint.jhash_header("Retrieve Zone ID - POST CALL - Output List", space=True)
cprint.jhash_header("AP of MAC {} Exists already", space=True)

cprint.jhash_header("AP with MAC {} Has Been Created", space=True)

cprint.jhash_header("TEST THESE MACS FIRST", space=True)

"""

list_mac = jspreadsheet.get_list_mac_hosts(SPREADSHEET="WAP info for SmartZone.xlsx", WORKSHEET="H510")

for macs in list_mac:
    print("{}".format(macs['name']))
    print("{}".format(macs['mac']))
    print("{}".format(macs['location']))
    print()
"""