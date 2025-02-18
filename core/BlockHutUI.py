import os
import time
import pathlib as Path
import json
import sys
import keyboard


CurrentMenu = "MainMenu"
KeyboaordInput = ""

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

#GUI art  defined here :
class Art:
    Header = """
|=[venv]==================================================[A0.1]=|
|             ▄▄                               .-.-----------.-. |
| ▀███▀▀▀██▄▀███                 ▀███          | |-----------|#| |
|   ██    ██  ██                   ██          | |-HUT---CLI-| | |
|   ██    ██  ██   ▄██▀██▄ ▄██▀██  ██  ▄██▀    | |-----------| | |
|   ██▀▀▀█▄▄  ██  ██▀   ▀███▀  ██  ██ ▄█       | |VERSION 0.1| | |
|   ██    ▀█  ██  ██     ███       ██▄██       | "-----------' | |
|   ██    ▄█  ██  ██▄   ▄███▄    ▄ ██ ▀██▄     |  .-----.-..   | |
| ▄████████ ▄████▄ ▀█████▀ █████▀▄████▄ ██▄    |  |     | || ||| |
|                                              |  |     | || \/| |
|                                              "--^-----^-^^---' |
|================================================================|"""

class MenuTextures:
    MainMenu = """|>>>[ Enter a Selection ]<<<=====================================|
|       [1] Install a package   |   [4] Download from URL        |
|       [2] Install Repository  |   [4] Run Setup Script BROKEN  |
|       [3] Open Package Scout  |   [5] Setup ServerHut          |
|                               |   [6] Quit                     |
|================================================================|
| [Block Hut GUI]                                                |
|                                                                |
|                                                                |
|                                                                |
|                                                                |
| For More Documentation, check My site                          |
|                        └>   http://kevinblog.sytes.net/?p=212  |
|================================================================|
"""

    PackageScout = """|>>>[Package Scout]<<<===========================================|
| [] 1.Random Package... name ig ?                              █|
|                                                               V|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|                                                               ║|
|================================================================|


"""




def RenderMenu(Menu):
     match Menu:
            case "MainMenu":
               print(MenuTextures.MainMenu)
            case "Scout":
               print(MenuTextures.PackageScout)
               
               

def UpdateScreen():
        clearScreen()
        print(Art.Header)
        RenderMenu(CurrentMenu)

        print(KeyboaordInput)

        GetKeyboardInput()
        pass




def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def GetKeyboardInput():
    global KeyboaordInput
    KeyboaordInput = input()
    UpdateScreen()
    return(KeyboaordInput)


UpdateScreen()

