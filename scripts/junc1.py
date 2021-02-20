import pathlib #File navigation and tools
pathlib.Path(__file__).parent.absolute() #Pathlib init
dirPath = pathlib.Path().absolute() #Current parent's path
realPath = dirPath/r'CMD-Notif' #Real working directory
scriptsPath = realPath/r'scripts' #Script storage directory

print('notif | Welcome to CMD-Notif! You can now type commands. Use \'help\' to view commands')
exec(open(scriptsPath/"commandline.py").read())