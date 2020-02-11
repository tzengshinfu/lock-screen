import os
import sys
import keyboard

while True:
    try:
        if keyboard.is_pressed(sys.argv[-1]):
            os.system('C:\\Windows\\System32\\rundll32.exe User32.dll,LockWorkStation')

    except:
        print('參數必須是按鍵名稱(如:F1/A/ESC)')
        break
