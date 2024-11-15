import pyautogui
import time
import keyboard
import win32api, win32con

pyautogui.displayMousePosition()
def click(x,y):
    win32api.((x,y))SetCursorPos