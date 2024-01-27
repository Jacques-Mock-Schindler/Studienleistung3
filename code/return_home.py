import utime
import math
import random
from microbit import *
from mbrobot import *

RobotContext.enableTrace(True)

def time_to_rad(time):
    degree = 360 / 2150 * time
    return math.radians(degree)

bewegungs_log = []

def log_bewegung(ereignis):
    timestamp = utime.ticks_ms()
    eintrag = [timestamp, ereignis]
    bewegungs_log.append(eintrag)

def ausfahrt():
    log_bewegung("Ausfahrt")
    time = random.randrange(500,2000,500)
    forward()
    delay(time)
    stop()

def drehung():
    log_bewegung("Drehung")
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
    log_bewegung("Zurücksetzen")
    backward()
    delay(500)
    stop()

def geradeausfahrt():
    start_time = utime.ticks_ms()  # Startzeit in Millisekunden
    duration = 60 * 1000  # Dauer in Millisekunden (1 Minute)
    
    forward()
    log_bewegung("Vorwärts")
    while True:
        # Prüfen, ob die Fahrtzeit abgelaufen ist
        if utime.ticks_diff(utime.ticks_ms(), start_time) >= duration:
            break

        # Kontinuierliche Distanzmessung
        d = getDistance()
        if d < 5:
            zuruecksetzen()
            drehung()
            forward()
            log_bewegung("Vorwärts")
        
        # Fügen Sie eine kleine Verzögerung ein, um den Prozessor nicht zu überlasten
        utime.sleep_ms(100)
    
    # Anhalten des Roboters nach 1 Minute
    stop()
    
ausfahrt()
drehung()
forward()
delay(2000)
print(bewegungs_log)

