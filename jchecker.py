"""
Author: Justin Francisco
Date Written: 29/03/2023
Last Modified By: Justin Francisco

Description: Checkers with Regex
Verify MAC Addresses and any numbers specified
Dependencies: re

"""
import re


def check_mac_validity(mac_address):
# 341593017F00
# 34:15:93:01:7F:00
    pass

# RUCKUS MAC FORMAT E.G.
# 341593017F00

def check_ruckus_mac(mac_address):
    if re.match(r"^([0-9a-fA-F]{2}:){5}([0-9a-fA-F][0-9a-fA-F])$",mac_address):
        pass
    if re.match(r"^(341593)([0-9a-fA-F]{6})$",mac_address):
        chunks = [mac_address[i:i+2] for i in range(0, len(mac_address), 2)]
        newmac = ":".join(chunks)
        return newmac
    else:
        pass

def host_name_checker(hostname):
    if re.match(r"^(B([0-9]){2}-L([0-9]){2}-R([0-9]){2})$",hostname):
        print("""
              Valid Hostname Address
              """)
        return True
    else:
        print("You inputted: {} \n This is not a valid Hostname".format(hostname))
        print("""        
Please Check the Following:
- Have two dash (-) separators
- 1st portion should start with B, BXX (XX = Building Number)
- 2nd portion should start with L, LXX (XX = Floor Number e.g. 1F)
- 2nd portion should start with R, RXX 
- FORMAT should be of BXX-LXX-RXX e.g. B98-L76-R54
              """)
        return False
    
def create_border(sentence):
    sentence_length = len(sentence)
    border = '#' +'-' * (sentence_length + 4)
    output = f"\n{border}\n#  {sentence} |\n{border}\n "
    return output
