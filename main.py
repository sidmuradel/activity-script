import pyautogui
import time
import random

min_mouse = 80
max_mouse = 90
min_scrolling = 2
max_scrolling = 6
min_shift = 6
max_shift = 12
min_idle_time = 20
max_idle_time = 30

time_goal = 2  # minutes
loop = 1  # minutes


screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

mid_screenW = screenWidth / 2
mid_screenH = screenHeight / 2

t_goal = time.time() + 60 * time_goal

while time.time() < t_goal:
    t_loop = time.time() + 60 * loop
    while time.time() < t_loop:
        randomScreenW = mid_screenW + random.randint(mid_screenW*-1/2, mid_screenW*1/2)
        randomScreenH = mid_screenH + random.randint(mid_screenH*-1/2, mid_screenH*1/2)
        if random.randint(0, 100) < random.randint(min_idle_time , max_idle_time):
            time.sleep(5)
        else:
            if random.randint(0, 100) < random.randint(min_mouse, max_mouse):
                pyautogui.moveTo(randomScreenW, randomScreenH, duration=2, tween=pyautogui.easeInOutQuad)
            else:
                for i in range(1, 10):
                    pyautogui.scroll(-50)
                for i in range(1, 10):
                    pyautogui.scroll(50)
                for i in range(1, random.randint(15, 30)):
                    pyautogui.press('shift')
                time.sleep(2)

