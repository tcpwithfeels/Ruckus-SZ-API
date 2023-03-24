# Project Title
## Description
Allows API Interaction with Ruckus Smart Zone 100 Wireless Controller

## Usage
Two ways to operate the script. 
If there is an argument specified then the script will read the spreadsheet specified for e.g. "List_WAPs.xlxs"
And go through each line and add APs to the controller.
EXAMPLE python python_script.py argument -flag

How to operate the script. Use code syntax: 
*`python ruckus_AP_add.py <name_of_spreadsheet>`*
`python ruckus_AP_add.py List_WAPs.xlxs`

Important notes in **BOLD** or *ITALICS* or **_BOTH_**

## Dependencies
The following libraries are dependancies
- requests, openpyxl
- second required library
> Consider packaging required pip modules with the project for portability

## Author
Auther: Justin Francisco Ma

Credit to Craig who wrote the cprint function - https://github.com/Phatkone


# FEELING SCRIPTY #

![image](https://user-images.githubusercontent.com/125618256/227404147-21825174-d69e-4f10-b0fa-bf497cdab6c8.png)


## Git-ting GUD
Ruckus-SZ-API
Mass adding of Ruckus Wireless Access Points

Initilize Git in CWD
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git init

Initialized empty Git repository in C:/Users/JustinFrancisco/Documents/Ruckus-Code/.git/

git remote add cbr https://github.com/tcpwithfeels/Ruckus-SZ-API.git

git pull cbr

remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 638 bytes | 42.00 KiB/s, done.
From https://github.com/tcpwithfeels/Ruckus-SZ-API
 * [new branch]      main       -> cbr/main  
 
git add . -v
add 'cprint.py'
add 'ruckus_AP_add.py'

git commit -m "cbr" 

[master (root-commit) ec89ca7] cbr
 2 files changed, 106 insertions(+)
 create mode 100644 cprint.py
 create mode 100644 ruckus_AP_add.py
 
git push cbr master

Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/tcpwithfeels/Ruckus-SZ-API/pull/new/master
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
 * [new branch]      master -> master

git branch

* master

git branch testing - 
git checkout testing
Switched to branch 'testing'

git add . -v

add 'ruckus_AP_add.py'

git commit -m "testb"

[testing 4bc1175] testb
 1 file changed, 2 insertions(+)
 
git checkout master

Switched to branch 'master'

git merge testing 

Updating ae83f34..4bc1175
Fast-forward
 ruckus_AP_add.py | 2 ++
 1 file changed, 2 insertions(+)

git push cbr --delete testing

To https://github.com/tcpwithfeels/Ruckus-SZ-API.git

 - [deleted]         testing

