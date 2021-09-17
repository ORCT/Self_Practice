#next page button position (468,56)
#go to first page (403,52)
#I want to capture that mouse click the next page button
#1. click button
#2. press capture key
#3. do 1~2 over and over#
import pyautogui
import time
import keyboard

pyautogui.click(x = 403, y = 52)

while 1:
    pyautogui.keyDown('alt')
    time.sleep(0.5)
    pyautogui.press('f1')
    pyautogui.keyUp('alt')
    time.sleep(0.5)
    pyautogui.click(x = 468, y = 56)
    if keyboard.is_pressed('enter'):
        break