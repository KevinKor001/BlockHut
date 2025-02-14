import os
import time
import pathlib as Path
import json
import sys
#config File Template :
PcfgFile ={
    "RepositoryDirectory": "^",
    "TRF" : False

}
cfgFile = json.dumps(PcfgFile)

#will be repository Listing:
Repositories = "https://kevinblog.sytes.net/hut"

UserDirectory = os.path.expanduser("~")
ConfigDir =  ""



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#test Colors,
print(bcolors.BOLD + bcolors.FAIL + "If this is bold , colors WORK!!!! 😁" + bcolors.ENDC)

def CreateConfigDir():
    print("Creating Directory Structure")
    ConfigFile = open(UserDirectory + "/.BlockHut/bh.config", "w")
    ConfigFile.write(str(repositories))
    ConfigFile.close()


time.sleep(0)

print("Detected Os : " , os.name)
if os.name != "posix":
    print(bcolors.HEADER + "Warning: Windows / MacOS not yet fully implemented, may look wierd or crash :)")

print("Checking Config Folder")
if os.path.exists(UserDirectory + "/.BlockHut/bh.config"):
    print("Proceeding!")
    ConfigDir = UserDirectory + "/.BlockHut"
    print("Arguments: ", sys.argv)
else:
    CreateConfigDir()

if sys.argv[1] == "install" or sys.argv[1] == "get":





