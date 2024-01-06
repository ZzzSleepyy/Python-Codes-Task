import pyautogui as s
import time as tulog

sleep = tulog.sleep

bilang = 15

while bilang != 2770:
    sleep(1)
    bilang = bilang + 1
    s.write(f"{bilang}")
    
    s.press("enter")
    
