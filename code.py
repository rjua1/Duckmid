from adafruit_circuitplayground import cp
import time
import random

thresh = 2  #change in acceleration threshold
x0, y0, z0 = 0, 0, 0  #previous acceleration value
duck = ["duck1.wav", "duck2.wav", "duck3.wav"]  #duck sounds on CIRCUITPY

lasttime = time.monotonic() #gets current time
timer = 10  #quack ever __ seconds
last = 0   #records last quack time

RED = (255, 0, 0)
ORANGE = (255, 51, 0)
YELLOW = (255, 153, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (153, 0, 255)
rainbow = (RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE)


while True:

    ## Sparkle 1 of 10 neopixels with random colors
    pix = random.randint(0, 9)                  #choose 1 of 10 neopixels
    color = random.randint(0, len(rainbow) - 1) #choose random color from rainbow
    cp.pixels[pix] = rainbow[color]             #display color
    cp.pixels.fill((0, 0, 0))                   #clear color

    ## Check for sudden acceleration
    x1, y1, z1 = cp.acceleration
    if x1 - x0 > thresh or y1 - y0 > thresh or z1 - z0 > thresh:
        cp.pixels.fill((255, 0, 0))           #shine red
        i = random.randint(0, len(duck) - 1)  #choose random duck sound
        cp.play_file(duck[i])                 #play duck sound
    x0, y0, z0 = cp.acceleration              #set last accel to current accel

    ## Quack every (timer) seconds
    if time.monotonic() - lasttime > timer:
        cp.pixels.fill((0, 0, 255))          #shine blue
        i = random.randint(0, len(duck) - 1) #choose random duck sound
        cp.play_file(duck[i])                #play duck sound
        lasttime = time.monotonic()          #restart timer count down
