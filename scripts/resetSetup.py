import pathlib #File navigation and tools
pathlib.Path(__file__).parent.absolute() #Pathlib init
dirPath = pathlib.Path().absolute() #Current parent's path
realPath = dirPath/r'CMD-Notif' #Real working directory
scriptsPath = realPath/r'scripts' #Script storage directory

exec(open(scriptsPath/"setup.py").read())