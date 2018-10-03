
import time
import pyautogui


pyautogui.FAILSAFE = True
loopCount = 0
while 1:
    print(pyautogui.position())
    print("loop count:" + str(loopCount))
    pyautogui.click(2601, 195)
    time.sleep(1)
    pyautogui.click(2601, 195)
    for i in range(60):
        time.sleep(1)
        print(60 - i)
    loopCount += 1
