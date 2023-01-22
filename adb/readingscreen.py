from android_screen_monitor import ScreenMonitor

sm = ScreenMonitor()
sm.start()

text = sm.get_text()
print(text)