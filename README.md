# Project Title
## Description
Allows API Interaction with Ruckus Smart Zone 100 Wireless Controller

## Usage
Two ways to operate the script. 
If there is an argument specified then the script will read the spreadsheet called "List_WAPs.xlxs"
And go through each line and add APs to the controller.
EXAMPLE python python_script.py argument -flag

How to operate the script. Use code syntax: `python python_script.py argument -flag`
Important notes in **BOLD** or *ITALICS* or **_BOTH_**

## Dependencies
The following libraries are dependancies
- required library
- second required library
> Consider packaging required pip modules with the project for portability

## Author
Credit to anyone who worked on the code or provided code
yourself as author
[Your Git Username](Link to your git account)

## License
[GNU GPL 3.0](LICENSE) License applies.










# Ruckus-SZ-API
Mass adding of Ruckus Wireless Access Points

# Initilize Git in CWD
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git init

Initialized empty Git repository in C:/Users/JustinFrancisco/Documents/Ruckus-Code/.git/

The git remote add command takes two arguments:

A remote name, for example, origin
A remote URL, for example, https://github.com/OWNER/REPOSITORY.git

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> 

git remote add cbr https://github.com/tcpwithfeels/Ruckus-SZ-API.git

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git pull cbr
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 638 bytes | 42.00 KiB/s, done.
From https://github.com/tcpwithfeels/Ruckus-SZ-API
 * [new branch]      main       -> cbr/main  
 
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git add . -v
add 'cprint.py'
add 'ruckus_AP_add.py'
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git commit -m "cbr" 
[master (root-commit) ec89ca7] cbr
 2 files changed, 106 insertions(+)
 create mode 100644 cprint.py
 create mode 100644 ruckus_AP_add.py
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.26 KiB | 1.26 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/tcpwithfeels/Ruckus-SZ-API/pull/new/master
remote:
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
 * [new branch]      master -> master
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git merge --help     
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git add . -v    
add 'ruckus_AP_add.py'
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git commit -m "test"
[master ae83f34] test
 1 file changed, 15 insertions(+), 12 deletions(-)
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 463 bytes | 463.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
   ec89ca7..ae83f34  master -> master
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch
* master
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch testing
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch
* master
  testing
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git checkout testing
Switched to branch 'testing'
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git add . -v
add 'ruckus_AP_add.py'
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git commit -m "testb"
[testing 4bc1175] testb
 1 file changed, 2 insertions(+)

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr testing
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 302 bytes | 302.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'testing' on GitHub by visiting:
remote:      https://github.com/tcpwithfeels/Ruckus-SZ-API/pull/new/testing
remote:
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
 * [new branch]      testing -> testing

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git checkout master
Switched to branch 'master'

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git merge testing 
Updating ae83f34..4bc1175
Fast-forward
 ruckus_AP_add.py | 2 ++
 1 file changed, 2 insertions(+)

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch
* master
  testing
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git add . -v
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git commit -m "merge"
On branch master
nothing to commit, working tree clean
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr master
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
   ae83f34..4bc1175  master -> master
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git purge 
git: 'purge' is not a git command. See 'git --help'.

The most similar command is
        prune
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git prune   
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch
* master
  testing
  
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr master

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push testing

Please make sure you have the correct access rights
and the repository exists.
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git branch -a
* master
  remotes/cbr/main
  remotes/cbr/master
  remotes/cbr/testing

PS C:\Users\JustinFrancisco\Documents\Ruckus-Code> git push cbr --delete testing
To https://github.com/tcpwithfeels/Ruckus-SZ-API.git
 - [deleted]         testing
PS C:\Users\JustinFrancisco\Documents\Ruckus-Code>
