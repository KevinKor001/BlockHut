import os
import time
import pathlib as Path
import json
import sys

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

class Menus:
    MainMenu = """|>>>[ Enter a Selection    https://kevinblog.sytes.net/?p=212]<<<|
|       [1] Install a package   |   [2] Download from URL        |
|       [3] run Setup File      |   [4] Quit                     |
|================================================================|
"""

def UpdateScreen():
        clearScreen()
        print(Art.Header)
        print(Menus.MainMenu)
        pass




def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')



UpdateScreen()
