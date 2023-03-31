"""

Collab with Craig B.
https://github.com/Phatkone

"""

def cprint(string: str, type: str = "endc", bold: bool = False, underline: bool = False) -> None:
    colours = {
        'PURPLE': '\033[95m',
        'BLUE': '\033[94m',
        'CYAN': '\033[96m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
    }
    if type.upper() in ['PURPLE','BLUE','CYAN','GREEN','YELLOW','RED','BOLD','UNDERLINE']:
        s = colours[type.upper()]
        if bold:
            s = s + colours['BOLD']
        if underline:
            s = s + colours['UNDERLINE']
        print("{}{}{}".format(colours[type.upper()],string,colours['ENDC']))
    else:
        print(string)

def jprint_cmd_banner(prompt=None, banner="#"):
    if prompt == None:
        print("No Prompt Specified")
    else:
        printer = "--- {} ---".format(prompt)
        print("{}".format(banner*(len(printer))))
        print(printer)
        print("{}".format(banner*(len(printer))))

def jhash_header(prompt=None, space=False):
    if prompt == None:
        print("-"*10)
    else:
        if space:
            print()
        printer = "{} --- {} ---".format("#", prompt)
        print("{}{}".format("#","-"*(len(printer))))
        print("{}".format(printer))
        print("{}{}".format("#","-"*(len(printer))))
        if space:
            print()