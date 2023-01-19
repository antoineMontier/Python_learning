import pyautogui, time, os

def openADB(ip_adress, port=5555):
    command = "adb connect " + ip_adress + ":" + str(port)
    os.system(command)
    os.system("adb shell")

def closeADB(ip_adress, port=5555):
    command = "adb disconnect " + ip_adress + ":" + str(port)
    os.system("exit")

openADB("ip_adress")

os.system("input swipe 14 15 200 200")

time.sleep(5)

os.system("exit")
#closeADB("ip_adress")
