import pyperclip
import pyautogui
import time

print("Program started\n")
time.sleep(3)

with open("adb\\cmd.txt", "r") as commands:
    for line in commands:
        pyperclip.copy(line.strip())
        print(f"Coppied {line.strip()}")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(1)

print("\nAll done")
