import pyautogui, time, os, subprocess, cv2, pyperclip

def open_adb():
    ip_adress = str(input("what is the Ip adress or your android device ?"))
    print("connection")

    result = subprocess.run(['adb', 'connect', ip_adress+':5555'])

    if not result.returncode == 0:
        print("Command failed with error code: ", result.returncode)
        exit()

    print("entering adb shell, type 'exit' to exit")


def open_spotify():
    result = subprocess.run(["adb", "shell", "am", "start", "-a", "android.intent.action.MAIN", "-c", "android.intent.category.LAUNCHER", "-n", "com.spotify.music/.MainActivity"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if(result.stderr.decode() == ""):
        print("spotify opened successfully")
    else:
        print(result.stderr.decode())

def enter_likedSongs():
    subprocess.run(["adb", "shell", "input", "tap", '530', '2325'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '530', '440'])
    time.sleep(1)
    subprocess.run(["adb", "shell", "input", "text", "Liked"])
    subprocess.run(["adb", "shell", "input", "keyevent", "62"]) # Space key
    subprocess.run(["adb", "shell", "input", "text", "songs"])



#open_adb()
#open_spotify()
#time.sleep(5)
enter_likedSongs()