import os #Operating system tools
import json #Read/write JSON
import pathlib #File navigation and tools
import asyncio #Asyncronous actions
import sys #System
import argparse #Commandline
import time
from datetime import datetime #Date and time
pathlib.Path(__file__).parent.absolute() #Pathlib init

#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
filePath = pathlib.Path(__file__).absolute() #Current file's path
dirPath = pathlib.Path().absolute() #Current parent's path
realPath = dirPath/r'CMD-Notif' #Real working directory
storePath = realPath/r'store' #Data storage directory
scriptsPath = realPath/r'scripts' #Script storage directory
parser = argparse.ArgumentParser() #Argparse init
helptext = open(storePath/r's-help.txt', 'r')
readyhelptext = helptext.read()
reset = scriptsPath/"reset.py"
resetSetup = scriptsPath/"resetSetup.py"
prefs = open(storePath/r'preferences.json', 'r+')
#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

text1 = input("setup >>> ")
if text1 == 'help':
    print(readyhelptext)
    time.sleep(0.5)
    exec(open(resetSetup).read())
elif text1 == 'exit':
    print('Exiting setup.')
    exec(open(reset).read())
else:
    print('Unrecognised command!')
    time.sleep(0.5)