import pyautogui, time, os, subprocess, cv2, pyperclip, pytesseract

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
    time.sleep(.2)
    subprocess.run(["adb", "shell", "input", "tap", '500', '550'])

def read_onScreen():
    import subprocess

    result = subprocess.run(["adb", "shell", "dumpsys", "accessibility"], stdout=subprocess.PIPE)
    output = result.stdout.decode()

    # Extract the content of the current focused element
    if "mFocusedNode:" in output and "mText:" in output and "mTextSelectionEnd" in output:
        content = output.split("mFocusedNode:")[1].split("mText:")[1].split("mTextSelectionEnd")[0].strip()
        print(content)
    else:
        print("mFocusedNode, mText or mTextSelectionEnd not found in the output")

def screenshot():
    subprocess.run(["adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])
    subprocess.run(["adb", "pull", "/sdcard/screenshot.png", "."])


def read_screenshot(output_file):
    image = cv2.imread("screenshot.png")
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 11')
    with open(str(output_file), "w") as file:
        file.write(text)

def choose_music():
    subprocess.run(["adb", "shell", "input", "tap", '500', '1600'])

## double-call
def clean_results(file_in, file_out):
    with open(str(file_in) + ".txt", "r") as I:
        with open(str(file_out) + ".txt", "w") as W:
            for line in I:
                # Remove leading and trailing white spaces
                line = line.strip()
                if len(line) < 4:
                    continue
                if "®" in line or "Home" in line or "Your Library" in line or "Search" in line:
                    continue
                line = line.replace("\"", "").replace("“", "").replace("»", "").replace(")", "").replace("@", "").replace("<", "").replace(">", "").replace("(", "").replace("{", "").replace("}", "").replace("Gees", "").replace("[", "").replace("[", "").replace("]", "").replace("[", "").replace("*", "").replace(".", "").replace("|", "").replace("an ", "").replace("[", "").replace("AN ", "").replace("An ", "").replace("aN ", "")
                if line[1] == " ":
                    line = line[1:]
                elif line[2] == " ":
                    line = line[2:]
                elif line[3] == " ":
                    line = line[3:]
                line.strip()
                W.write(line + '\n')



#open_adb()
#open_spotify()
#time.sleep(6)
#enter_likedSongs()
#time.sleep(.5)
#read_onScreen()
#screenshot()
#read_screenshot("titles.txt")
#choose_music()
#clean_results("titles", "Titles")
#clean_results("Titles", "Titles2")
os.chdir('/home/antoine/Prog/python/first/adb/music')
subprocess.run(['spotdl', 'download', 'https://open.spotify.com/track/5qaEfEh1AtSdrdrByCP7qR?si=kVzKnsJUQ3quQLoFE8ss1g'])