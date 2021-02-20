import os #Operating system tools
import json #Read/write JSON
import pathlib #File navigation and tools
import asyncio #Asyncronous actions
from datetime import datetime #Date and time
#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
pathlib.Path(__file__).parent.absolute()
filePath = pathlib.Path(__file__).absolute() #Current file's path
dirPath = pathlib.Path().absolute() #Current parent's path
realPath = dirPath/r'CMD-Notif' #Real working directory
storePath = realPath/r'store' #Data storage directory
scriptsPath = realPath/r'scripts' #Script storage directory
#!=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
open(realPath/r'store/preferences.json', 'x')
prefs = open(realPath/r'store/preferences.json', 'r+')