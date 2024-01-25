import random
import utime
from microbit import * 
from mbrobot import *

bewegungs_log = []

def log_bewegung(ereignis):
    timestamp = utime.ticks_ms()
    bewegungs_log.append(str(timestamp) + ' : ' + ereignis)
    


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
    duration = 20 * 1000  # Dauer in Millisekunden (1 Minute)
    
    forward()
    log_bewegung("Geradeausfahrt")
    while True:
        # Prüfen, ob die Fahrtzeit abgelaufen ist
        if utime.ticks_diff(utime.ticks_ms(), start_time) >= duration:
            break

        # Kontinuierliche Distanzmessung
        d = getDistance()
        if d < 5:
            zuruecksetzen()
            drehung()
            log_bewegung("Geradeausfahrt")
            forward()
        
        # Fügen Sie eine kleine Verzögerung ein, um den Prozessor nicht zu überlasten
        utime.sleep_ms(100)
    
    # Anhalten des Roboters nach 1 Minute
    stop()
    log_bewegung("Stop")



ausfahrt()
drehung()
geradeausfahrt()
print(bewegungs_log)












