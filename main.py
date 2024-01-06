# import pyautogui
# from ahk import AHK
import mouse
import cv2

import pygetwindow as gw
import time
import keyboard
import random

# ahk = AHK()

def click():
    # pyautogui.mouseDown()
    # time.sleep(0.01)
    # pyautogui.mouseUp()
    # mouse.click()
    mouse.press()
    time.sleep(0.1)
    mouse.release()




def getCoordinates():
    # current_x, current_y = pyautogui.position()
    # coords = ahk.get_mouse_position(coord_mode='Screen')
    coords = mouse.get_position()
    
    print(f"Текущие координаты X, Y: {coords}")
    # print(f"Текущие координаты X, Y: {current_x}, {current_y}")

def smooth_move():
    card_type = int(input('Type card type (1/2/3/4): '))
    iteration_count = int(input("Card count: "))

    time.sleep(1)

    # pyautogui.moveTo(10, 10, 1, pyautogui.easeInOutQuad)
    mouse.move(10, 10, True, 0)
    click()

    print('Move started...')
    # time.sleep(2)

    coords = [
        # [894, 840]
        [791, 283],
        [1017, 284],
        [1275, 272],
        [821, 475],
        [1222, 469],
    ]

    match card_type:
        case 1:
            coords.append([575, 835])
        case 2:
            coords.append([653, 833])
        case 3:
            coords.append([1384, 826])
        case 4:
            coords.append([1452, 834])

    for i in range(iteration_count):
        n = 0
        coord_length = len(coords)
        time.sleep(0.2)

        for coord in coords:
            n += 1
            print('Next card')
            # rand_move_time = (random.randint(1, 2)/8)
            move_time = 0.2
            '''
            pyautogui.moveTo(coord[0], coord[1], randMoveTime, pyautogui.easeInOutQuad)
            click()
            ahk.mouse_move(coord[0], coord[1], speed=10, relative=False)
            ahk.click()
            '''

            mouse.move(coord[0], coord[1], True, move_time)
            click()

            print('Clicked...')

            if (n == coord_length):
                time.sleep(1.5)
                click()

# def get_avaliability_status_card():
    

keyboard.add_hotkey('ctrl+alt+d', getCoordinates)
keyboard.add_hotkey('ctrl+alt+f', smooth_move)

keyboard.wait()
