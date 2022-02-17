# InvisibilityCloak - a reason to tinker with image processing in Python motivated by being too frugal to buy the official toy
# Invisibility_Cloak © 2021 is licensed under Attribution-NonCommercial 4.0 International

import cv2
import numpy as np
import time


def set_background(cam):
    ret, background = cam.read()
    background = np.flip(background, axis=1)
    print("Background Set")
    return background


def process_keyboard(k):

    # Adjust Mask HSV upper limits
    if k == 49:
        mask_hsv_lower_limit[0] += 10
        print("low_h", mask_hsv_lower_limit[0])
    if k == 50:
        mask_hsv_lower_limit[1] += 10
        print("low_s", mask_hsv_lower_limit[1])
    if k == 51:
        mask_hsv_lower_limit[2 ] += 10
        print("low_v", mask_hsv_lower_limit[2])
    if k == 113:
        mask_hsv_lower_limit[0] -= 10
        print("low_h", mask_hsv_lower_limit[0])
    if k == 119:
        mask_hsv_lower_limit[1] -= 10
        print("low_s", mask_hsv_lower_limit[1])
    if k == 101:
        mask_hsv_lower_limit[2] -= 10
        print("low_v", mask_hsv_lower_limit[2])

    # Adjust Mask HSV lower limits
    if k == 97:
        mask_hsv_upper_limit[0] += 10
        print("high_h", mask_hsv_upper_limit[0])
    if k == 115:
        mask_hsv_upper_limit[1] += 10
        print("high_s", mask_hsv_upper_limit[1])
    if k == 100:
        mask_hsv_upper_limit[2] += 10
        print("high_v", mask_hsv_upper_limit[2])
    if k == 122:
        mask_hsv_upper_limit[0] -= 10
        print("high_h", mask_hsv_upper_limit[0])
    if k == 120:
        mask_hsv_upper_limit[1] -= 10
        print("high_s", mask_hsv_upper_limit[1])
    if k == 99:
        mask_hsv_upper_limit[2] -= 10
        print("high_v", mask_hsv_upper_limit[2])

    # Update the background image
    if k == 32:
        background = set_background(cam)



# Initialise mask levels (Green)
mask_hsv_lower_limit = [30, 0, 70]
mask_hsv_upper_limit = [80, 255, 255]

print("Invisibility Cloak")

# Capture static Background image
cam = cv2.VideoCapture(2)   # Internal camera
#cam = cv2.VideoCapture(1)   # External Camera
background = set_background(cam)

#Apply mask to live image
while (cam.isOpened()):

    #Get live camera image
    ret, img = cam.read()
    img = np.flip(img, axis=1)

    #Create Mask
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_lower_limit = np.array([mask_hsv_lower_limit[0], mask_hsv_lower_limit[1], mask_hsv_lower_limit[2]])
    mask_upper_limit = np.array([mask_hsv_upper_limit[0], mask_hsv_upper_limit[1], mask_hsv_upper_limit[2]])
    mask = cv2.inRange(hsv, mask_lower_limit, mask_upper_limit)

    # Remove small mask glithces
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    #Replace live image with background where masked
    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    #Display modified image
    cv2.imshow('Display', img)

    # Reset waitKey delay, which doubles as output frame rate control in m seconds
    k = cv2.waitKey(1)

    if k > -1:
        process_keyboard(k)

    # End While if Esc key pressed
    if k == 27:
        print("Decloaking")
        break

