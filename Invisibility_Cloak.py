import cv2
import numpy as np
import time

print("Invisibility Cloak")

# Initialise mask levels (Green)
low_h = 30
low_s = 0
low_v = 70
high_h = 80
high_s = 255
high_v =255

# Capture static Background image
# cam = cv2.VideoCapture(0)   # Internal camera
cam = cv2.VideoCapture(1)   # External Camera
ret, background = cam.read()
background = np.flip(background, axis=1)

#Apply mask to live image
while (cam.isOpened()):

    ret, img = cam.read()
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # value = (35, 35)
    # blurred = cv2.GaussianBlur(hsv, value,0)

    #Create Mask - Green
    lower_colour = np.array([low_h, low_s, low_v])
    upper_colour = np.array([high_h, high_s, high_v])
    mask = cv2.inRange(hsv, lower_colour, upper_colour)


    # Remove small mask glithces
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    #Modify image where masked
    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    #Display modified image
    cv2.imshow('Display', img)

    # Reset waitKey delay, which doubles as output frame rate control in m seconds
    k = cv2.waitKey(1)

    # Adjust Mask HSV upper limits
    if k == 49:
        low_h += 10
        print("low_h", low_h)
    if k == 50:
        low_s += 10
        print("low_s", low_s)
    if k == 51:
        low_v += 10
        print("low_v", low_v)
    if k == 113:
        low_h -= 10
        print("low_h", low_h)
    if k == 119:
        low_s -= 10
        print("low_s", low_s)
    if k == 101:
        low_v -= 10
        print("low_v", low_v)

    # Adjust Mask HSV lower limits
    if k == 97:
        high_h += 10
        print("high_h", high_h)
    if k == 115:
        high_s += 10
        print("high_s", high_s)
    if k == 100:
        high_v += 10
        print("high_v", high_v)
    if k == 122:
        high_h -= 10
        print("high_h", high_h)
    if k == 120:
        high_s -= 10
        print("high_s", high_s)
    if k == 99:
        high_v -= 10
        print("high_v", high_v)

    # Update the background image
    if k == 32:
        ret, background = cam.read()
        background = np.flip(background, axis=1)
        print("Background Updated")

    # End While if Esc key pressed
    if k == 27:
        print("Decloaking")
        break

