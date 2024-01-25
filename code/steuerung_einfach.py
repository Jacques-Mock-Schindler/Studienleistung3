import random
from microbit import * 
from mbrobot import *

def ausfahrt():
    time = random.randrange(500,2000,500)
    forward()
    delay(time)
    stop()

def drehung():
    time = random.randrange(200,1100,50)
    direction = random.choice([1,-1])
    if direction == 1:
        left()
        delay(time)
        stop()
    else:
        right()
        delay(time)
        stop()

def zuruecksetzen():
    backward()
    delay(500)
    stop()

def geradeausfahrt():
    forward()
    repeat:
        d = getDistance()
        if d < 5:
            zuruecksetzen()
            drehung()
            geradeausfahrt()


ausfahrt()
drehung()
geradeausfahrt()












