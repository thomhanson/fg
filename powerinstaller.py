import random, sys, os, subprocess, getpass, time
from os.path import exists
no = False

#get user of PC
try:
    user = getpass.getuser()
except OSError:
    try:
        user = os.getlogin()
    except OSError:
        try:
            user = os.path.expanduser()
        except OSError:
            try:
                user = os.environ.get()
            except OSError:
                try:
                    user = os.getuid()
                except OSError:
                    from pathlib import Path
                    user = Path.home().name

# checks if modules are found and if not asks the user to install them self or the program
try:
    import tkinter as tk
    import requests, shutil, string
except ModuleNotFoundError:
    t = input("Needed modules cant be found want to install? (Y/N) ")
    n = t.lower()
    if n == "y":
        subprocess.Popen("python -m pip install --upgrade requests shutil string && python -m pip install requests shutil string", shell=True)
    else:
        sys.exit(1)

apps = ["python", "steam", "roblox", "google", "roblox_bot_1", "roblox_bot_2"]

def randomize_same_pattern(code):
    result = []

    for char in code:
        if char.isdigit():
            result.append(random.choice(string.digits))
        elif char.isalpha():
            result.append(random.choice(string.ascii_uppercase))
        else:
            result.append(char)

    return ''.join(result)

def install_app(app):
    print(f"Installing {app}...")

    try:
        import pydirectinput
        import ctypes
        import keyboard
    except ModuleNotFoundError:
        subprocess.Popen("python -m pip install ctypes pydirectinput pynput keyboard")

    if app == "python":
        url = "https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe"
    elif app == "steam":
        url = "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe"
    elif app == "roblox":
        roblox_thingy = randomize_same_pattern("HDTE33THG7")
        url = f"https://www.roblox.com/download/client?token={roblox_thingy}"
        print("theres a 50/50 chance for it to work if it does not have the roblox icon then it did not work and you have to run this agen")
    elif app == "roblox_bot_1":
        global roblox_bot_1
        with open("roblox_bot_1.py", "w", encoding="utf-8") as f:
            f.write(roblox_bot_1)
        
        print("made roblox_bot_1.py just open it in cmd and it shold be good to go! :)")
        return
    elif app == "roblox_bot_2":
        global roblox_bot_2
        with open("roblox_bot_2.py", "w", encoding="utf-8") as f:
            f.write(roblox_bot_2)
        
        print("made roblox_bot_2.py this is not made and will not work but is on the work for the game: Roblox Cookie Clicker")
        return

    if app == "roblox":
        local_filename = f"RobloxPlayerInstaller-{roblox_thingy}.exe"
    else:
        local_filename = url.split('/')[-1]

    try:
        print(f"Downloading {local_filename}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print("Download complete successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Download failed due to a network error: {e}")

def start_gui():
    root = tk.Tk()
    root.title("Power Installer")

    tk.Label(root, text="Select an app to install:").pack(pady=10)

    for app in apps:
        tk.Button(root, text=f"Install {app}", command=lambda a=app: install_app(a)).pack(pady=5)

    root.mainloop()

# checks if all is there
if not exists(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules"):
    os.mkdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules")
if not exists(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\version.txt"):
    os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules")
    with open("version.txt", "w") as f:
        f.write("1.0.0")
os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER")
if not exists("config.txt"):
    with open("config.txt", "w") as f:
        f.write("")

os.chdir("Modules")
if not exists("updater.bat"):
    os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER")
    with open("config.txt", "r") as f:
        try_down = f.readlines()
    for line in try_down:
        if line == "NO_UPDATE":
            down = False
            pass
        else:
            down = True

    if down:
        os.chdir("Modules")
        t = input("updater script does not exist want to install? (Y/N) ")
        n = t.lower()
        if n == "y":
            #remake batch file later
            with open("updater.bat", "w") as f:
                f.write(f"""@echo off \ntitle downloading: ver.txt \ncurl -L -o ver.txt \ntitle finding out what version this is \nif exist "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\ver.txt" (\n   for /f %%i in ('C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\ver.txt') do set N_version \n) \n if exist "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\version.txt" (\n   for /f %%i in ('C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\version.txt') do set old_version \n) \n if "%N_version%"=="%old_version%" (\n    title no new version \n    timeout 3 >nul \n    exit /b 0 \n) else (\n    title found new version! \n    curl -L -o powerinstaller.py \n    del /Q "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\powerinstaller.py" \n    move "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\Modules\\powerinstaller.py" "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\powerinstaller.py" \n    title done! \n    echo done! \n    timeout 3 >null \n    cd /d "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER" \n    echo NO_UPDATE>config.txt \n    python C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\powerinstaller.py \n     timeout 5 >nul \n    del /Q "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\config.txt" \n   echo d>config.txt \n   exit /b 0 \n) \ncd /d "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER" \necho NO_UPDATE>config.txt \npython C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\powerinstaller.py \ntimeout 5 >nul \ndel /Q "C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\config.txt" \necho d>config.txt \nexit /b 0""")
        if n == "n":
            os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER")
            with open("config.txt", "a") as f:
                f.write("NO_UPDATE")
        else:
            print(f"thats not a option i gess you dont want updater.bat to have it just delete config.txt in C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER\\config.txt")
            os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER")
            with open("config.txt", "a") as f:
                f.write("NO_UPDATE")
else:
    os.chdir(f"C:\\Users\\{user}\\AppData\\Local\\POWERINSTALLER")
    with open("config.txt", "r") as f:
        text = f.readlines()
        for i in text:
            if i == "NO_UPDATE":
                no = True
    
    if no:
        pass
    else:
        if len(sys.argv) > 0:
            if sys.argv[1] == "-NOAUTOUPDATE":
                if len(sys.argv) < 3:
                    print("powerinstaller.py -H or powerinstaller.py -NOAUTOUPDATE -H for more commands")
                    sys.exit(0)

                if sys.argv[2] == "-H" or sys.argv[2] == "-h":
                    print("-inst for installing an app")
                    print("-inst -H for help with -inst")
                    print("-GUI for starting the program in GUI mode")
                    print("-st for starting apps")
                    print("-NOAUTOUPDATE")
                    sys.exit(0)

                elif (sys.argv[2] == "-inst" and len(sys.argv) > 3 and (sys.argv[3] == "-H" or sys.argv[3] == "-h")):
                    print("Available apps to install:")

                    for app in apps:
                        print(f"-inst {app}")

                    sys.exit(0)

                elif sys.argv[2] == "-inst" and len(sys.argv) > 3:
                    app_to_install = " ".join(sys.argv[3:])

                    if app_to_install in apps:
                        install_app(app_to_install)
                    else:
                        print(f"Unknown app: {app_to_install}")
                        print("Use -inst -H or -NOAUTOUPDATE -inst -H for available apps")

                    sys.exit(0)

                elif sys.argv[2] == "-GUI":
                    start_gui()

                elif sys.argv[2] == "-st":
                    if not sys.argv[3]:
                        print("to use -NOAUTOUPDATE -st put the app (with . so for roblox it whold be -st RobloxPlayerInstaller.exe)")
                        sys.exit(1)

                    if exists(sys.argv[3]):
                        try:
                            os.startfile(sys.argv[3])
                        except OSError:
                            if sys.argv[3].endswith(".py"):
                                subprocess.run(["python", sys.argv[3]])
                            else:
                                print("error that kind of file can this program not start")
                                sys.exit(1)
                    sys.exit(0)
                else:
                    print("Invalid argument. Use -H or -NOAUTOUPDATE for help")
                    sys.exit(1)
                sys.exit(0)

#roblox_bot_1 is a bot for roblox game: Case Paradise
roblox_bot_1 = r"""
import time
import pydirectinput
import ctypes
import keyboard
import threading

ctypes.windll.shcore.SetProcessDpiAwareness(1)

running = False

gifts = {
    "open_gift": (960, 986),
    "gift_1": (727, 316),
    "gift_2": (959, 309),
    "gift_3": (1186, 315),
    "gift_4": (724, 513),
    "gift_5": (956, 515),
    "gift_6": (1188, 512),
    "gift_7": (729, 709),
    "gift_8": (958, 711),
    "gift_9": (1187, 714)
}

cases = {
    "open_cases": (495, 981),
    "arrows_right": (1093, 472),
    "start_spin": (975, 467),
    "open_case_1": (960, 414),
    "open_case_2": (471, 751),
    "open_case_3": (713, 756),
    "open_case_4": (962, 748),
    "open_case_5": (1203, 751),
    "open_case_6": (1452, 757),
    "sell_guns": (-337, 402),
    "return_after_sell": (638, 681)
}

def clat(x, y, delay=0.2):
    pydirectinput.moveTo(x, y)
    time.sleep(delay)
    pydirectinput.click()

def bot_loop():
    global running

    T = 8
    cases_open_thingy = 6
    plus_multi = 5
    times_to_use_same_case = 10

    while running:

        clat(*gifts["open_gift"])

        for i in range(1, T + 1):
            clat(*gifts[f"gift_{i}"])

        clat(*cases["open_cases"])

        for i in range(1, cases_open_thingy + 1):

            clat(*cases[f"open_case_{i}"])

            for _ in range(plus_multi):
                clat(*cases["arrows_right"])

            for _ in range(times_to_use_same_case):

                clat(*cases["start_spin"])

                time.sleep(8)

                clat(*cases["sell_guns"])
                clat(*cases["return_after_sell"])

def start_bot():
    global running

    if not running:
        running = True
        threading.Thread(target=bot_loop).start()
        print("Bot started")

def stop_bot():
    global running
    running = False
    print("Bot stopped")

keyboard.add_hotkey("F6", start_bot)
keyboard.add_hotkey("F7", stop_bot)

print("F6 = Start | F7 = Stop")

keyboard.wait()
"""

#roblox_bot_2 is for roblox game: Roblox Cookie Clicker
roblox_bot_2 = r"""
import time
import pydirectinput
import ctypes
import keyboard
import threading

ctypes.windll.shcore.SetProcessDpiAwareness(1)

running = False

upgrades = {
    "cl1": (1548, 370),
    "cl2": (1548, 440),
    "cl3": (1548, 510),
    "cl4": (1548, 580),
    "cl5": (1548, 650),
    "cl6": (1548, 730),
    "cl7": (1548, 800),
    "cl8": (1548, 870)
}

boot = {
    "clboot1": (-602, 204)
    "clboot2": (-602, 103)
    "clboot3": (-602, 2)
    "clboot4": (-602, -99)
    "clboot5": (-602, -200)
}

def clat(x, y, delay=0.2):
    pydirectinput.moveTo(x, y)
    time.sleep(delay)
    pydirectinput.click()

def bot_loop():
    global running

    CLtimes = 8
    CLBOOTtimes = 1
    clickedMAX = False

    while running:
        if not clickedMAX:
            clat(1860, 981)
            clickedMAX = True
        else:
            clat(296, 463)

        while CLtimes != 0:
            clat(*upgrades[f"cl{CLtimes}"])
            CLtimes - 1
        
        while CLBOOTtimes != 5:
            clat(*boot[f"clboot{CLBOOTtimes}"])
            CLBOOTtimes + 1
        

def start_bot():
    global running

    if not running:
        running = True
        threading.Thread(target=bot_loop).start()
        print("Bot started")

def stop_bot():
    global running
    running = False
    print("Bot stopped")

keyboard.add_hotkey("F6", start_bot)
keyboard.add_hotkey("F7", stop_bot)

print("F6 = Start | F7 = Stop")

keyboard.wait()
"""

if len(sys.argv) < 2:
    print("powerinstaller.py -H for more commands")
    sys.exit(0)

if sys.argv[1] == "-H" or sys.argv[1] == "-h":
    print("-inst for installing an app")
    print("-inst -H for help with -inst")
    print("-GUI for starting the program in GUI mode")
    print("-st for starting apps")
    print("-NOAUTOUPDATE")
    sys.exit(0)

elif (sys.argv[1] == "-inst" and len(sys.argv) > 2 and (sys.argv[2] == "-H" or sys.argv[2] == "-h")):
    print("Available apps to install:")

    for app in apps:
        print(f"-inst {app}")

    sys.exit(0)

elif sys.argv[1] == "-inst" and len(sys.argv) > 2:
    app_to_install = " ".join(sys.argv[2:])

    if app_to_install in apps:
        install_app(app_to_install)
    else:
        print(f"Unknown app: {app_to_install}")
        print("Use -inst -H for available apps")

    sys.exit(0)

elif sys.argv[1] == "-GUI":
    start_gui()

elif sys.argv[1] == "-st":
    if not sys.argv[2]:
        print("to use -st put the app (with . so for roblox it whold be -st RobloxPlayerInstaller.exe)")
        sys.exit(1)

    if exists(sys.argv[2]):
        try:
            os.startfile(sys.argv[2])
        except OSError:
            if sys.argv[2].endswith(".py"):
                subprocess.run(["python", sys.argv[2]])
            else:
                print("error that kind of file can this program not start")
                sys.exit(1)
    sys.exit(0)
else:
    print("Invalid argument. Use -H for help")
    sys.exit(1)
