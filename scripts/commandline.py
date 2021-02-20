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
helptext = open(storePath/r'help.txt', 'r')
readyhelptext = helptext.read()
reset = scriptsPath/"reset.py"
#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

text1 = input("notif >>> ")
if text1 == 'help':
    print(readyhelptext)
    time.sleep(1)
    exec(open(reset).read())
elif text1 == 'setup':
    print('notif | Entered setup.')
    exec(open(scriptsPath/r"setup.py").read())
else:
    print('Unrecognised command!')
    time.sleep(1)
    exec(open(reset).read())