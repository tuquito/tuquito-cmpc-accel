#!/usr/bin/python

import pygame
from pygame import joystick
from pygame import event
from pygame.locals import *
import os
import time

os.system("cellwriter --hide-window &")

pygame.init()
joystick.init()
num_dev = joystick.get_count()
accel = None
i = 0
while i < num_dev:
    accel = joystick.Joystick(i)
    try:
        accel.init()
    except pygame.error:
        print "Error initializing accelerator!"
        exit(1)
    i += 1
    if accel.get_numaxes() == 3:
        break

if not accel:
    print "No accelerator device found. Exiting..."
    exit(1)

def rotate(orientation):
    print "Rotate " + orientation
    os.system('rotate %s &' % orientation)
    return orientation

orientation = rotate("inverted")
while True:
    time.sleep(0.5)
    for ev in event.get():
        if ev.type == QUIT:
            joystick.quit()
            pygame.quit()
            exit(0)

        if ev.type == JOYAXISMOTION:
            axis_x = accel.get_axis(0)
            axis_y = accel.get_axis(1)
            axis_z = accel.get_axis(2)
            if (axis_x > 0.25) and (orientation != "left"):
                orientation=rotate("left")
            elif (axis_x < -0.2) and (orientation != "right"):
                orientation=rotate("right")
            elif (axis_x < 0.3) and (axis_x > -0.2) and (axis_y < -0.1) and (orientation != "normal"):
                orientation=rotate("normal")
            elif (axis_x < 0.3) and (axis_x > -0.2) and (axis_y > 0.3) and (orientation != "inverted"):
                orientation=rotate("inverted")
