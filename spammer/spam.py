import pyautogui as pg
import time

def write_function(how_many_times):
    for i in range(how_many_times):
        pg.typewrite(":c")
        pg.press("enter")

def main():
    time.sleep(1)
    write_function(10)

main()
