import ctypes
import pyautogui
import datetime
import threading as th
import time
import random

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)

keep_going = True
def key_capture_thread():
    global keep_going
    #enter key pressed = stop program
    input()
    keep_going = False

def move_mouse():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        width = random.randrange(0,screenWidth)
        height = random.randrange(0,screenHeight)
        print("{}: moving... w: {} h: {}".format(datetime.datetime.now(), width, height))
        pyautogui.moveTo(width, height, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.press('up')

        time.sleep(60)

move_mouse()
print("Exiting")

