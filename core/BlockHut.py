import os
import time
import pathlib as Path
import json
import sys
import tqdm
import requests

#config File Template :
PcfgFile ={
    "RepositoryDirectory": "^",
    "TRF" : False

}
cfgFile = json.dumps(PcfgFile)

#will be repository Listing:
Repositories = "https://kevinblog.sytes.net/hut"
Arguments = []
UserDirectory = os.path.expanduser("~")
ConfigDir =  ""
FileLink = ""
FileName = ""
ChunkSize = 1024

#arguments :
class ArgumentValues:
    ImediateInstall = False
    SearchCustomRep = False
    CustomRep = ""
    ApplicationCandidate = ""
    ApplicationVersion = ""
    SavePath = ""

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
    ConfigFile.write("hi")
    ConfigFile.close()

def ConfigureArguments():
    global FileLink, FileName
    print("Setting Values")
    print(bcolors.BOLD + bcolors.WARNING + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + bcolors.ENDC)
    match Arguments[0]:
        
        case "install":
            
            ArgumentValues.ImediateInstall = True
            ArgumentValues.ApplicationCandidate = Arguments[1]
            if Arguments[2] == "":
                ArgumentValues.ApplicationVersion = "Latest"
            else:
                ArgumentValues.ApplicationVersion = Arguments[2]
                FileLink = Repositories + "/" + ArgumentValues.ApplicationCandidate + "/" + ArgumentValues.ApplicationVersion
                FileName = ArgumentValues.ApplicationCandidate + "-" + ArgumentValues.ApplicationVersion + ".zip"
   
            
        case "fetch":
            ArgumentValues.ImediateInstall = True
            ArgumentValues.ApplicationCandidate = Arguments[1]
            ArgumentValues.ApplicationVersion = "Fetched"
            FileLink = Arguments[2]
            FileName = ArgumentValues.ApplicationCandidate + "-" + ArgumentValues.ApplicationVersion + ".zip"



print("Detected Os : " , os.name)
if os.name != "posix":
    print(bcolors.HEADER + "Warning: Windows / MacOS not yet fully implemented, may look wierd or crash :)")

print("Checking Config Folder")
if os.path.exists(UserDirectory + "/.BlockHut/bh.config"):
    print("Proceeding!")
    ConfigDir = UserDirectory + "/.BlockHut"
    Arguments = sys.argv
    Arguments.pop(0)
    print("Arguments: ", Arguments)
    ConfigureArguments()

    print(ArgumentValues.ImediateInstall)
    print(ArgumentValues.ApplicationCandidate)
    print(ArgumentValues.ApplicationVersion)
    print(bcolors.BOLD + bcolors.WARNING + "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + bcolors.ENDC)
    ArgumentValues.SavePath = os.path.join(os.getcwd(), FileName)
    print(bcolors.OKGREEN + "File Name : " + bcolors.BOLD +bcolors.FAIL + FileName + bcolors.ENDC)
    print(bcolors.OKGREEN + "File Location : " + bcolors.BOLD +bcolors.FAIL + ArgumentValues.SavePath + bcolors.ENDC)
    print(bcolors.OKGREEN + "File Link : " + bcolors.BOLD +bcolors.FAIL + FileLink + bcolors.ENDC)

else:
    CreateConfigDir()

#if ArgumentValues.ImediateInstall == True:
#    r = requests.get(FileLink, stream=True)
#    totalSize = int(r.headers['content-length'])
#
#    with open(FileName, "wb") as file:
#        for data in tqdm(r.iter_content(chunk_size= ChunkSize), totalSize/ChunkSize, "KB"):
#            file.write(data)

print("Download Complete")



