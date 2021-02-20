import os #Operating system tools
import json #Read/write JSON
import pathlib #File navigation and tools
import asyncio #Asyncronous actions
import sys #System
import argparse #Commandline
from datetime import datetime #Date and time
pathlib.Path(__file__).parent.absolute() #Pathlib init

#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
filePath = pathlib.Path(__file__).absolute() #Current file's path
dirPath = pathlib.Path().absolute() #Current parent's path
realPath = dirPath/r'CMD-Notif' #Real working directory
storePath = realPath/r'store' #Data storage directory
scriptsPath = realPath/r'scripts' #Script storage directory
parser = argparse.ArgumentParser() #Argparse init
args = parser.parse_args()
prefs = open(storePath/r'preferences.json', 'r')
#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if os.path.isfile(storePath/r'preferences.json') is True:
    print('notif | Found preferences, loading.')
else:
    print('notif | Preferences not found! Creating now.')
    print('Thank you for using CMD-Notif!')
    open(realPath/r'store/preferences.json', 'x')

text = input("notif | Done. Press enter to continue.")
exec(open(scriptsPath/r"junc-CL.py").read())