# Ruckus Smart Zone API Script
## Description
Allows API Interaction with Ruckus Smart Zone 100 Wireless Controller

## Usage
Two ways to operate the script. 
If there is an argument specified then the script will read the spreadsheet specified for e.g. "List_WAPs.xlxs"
And go through each line and add APs to the controller.
EXAMPLE python python_script.py argument -flag

How to operate the script. Use code syntax: 
`python RuckusSZ_API_Interaction.py credentials.json`

Credentials contain the .. credentials
FORMAT
{
    "smartzone_info" : {
        "host" : "<hostname>",
        "api_version" : "v8_2"
    },
    "credz" : {
        "username" : "<username>",
        "password" : "<password>"
    }
}

Replace hostname, username and password and api_version (if app)
If json file not specified, then it will prompt you for all of the above

Important notes in **BOLD** or *ITALICS* or **_BOTH_**

## Dependencies
The following libraries are dependancies
- requests, openpyxl 
- re (Regex for MAC Address Checking)
> Consider packaging required pip modules with the project for portability

## Author
Auther: Justin Francisco Ma

Credit to Craig who wrote the cprint function - https://github.com/Phatkone

# FEELING SCRIPTY #

![image](https://user-images.githubusercontent.com/125618256/227404147-21825174-d69e-4f10-b0fa-bf497cdab6c8.png)

## Git-ting GUD

Usage: `python RuckusSZ_API_Interaction.py credentials.json`
