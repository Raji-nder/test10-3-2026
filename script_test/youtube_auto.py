import webbrowser
import pyautogui
import time
# 🔹 Put your YouTube video URL here
video_url = "https://youtube.com/shorts/TajAzT3CVJc?si=sJc_hxhHuKVJe3ds"
# Open YouTube video
webbrowser.open(video_url)
# Increase system volume to maximum
for i in range(50):   # 50 presses = full volume
 pyautogui.press("volumeup")
   

