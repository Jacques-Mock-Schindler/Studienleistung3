# Ein letzter Versuch, die Rückfahrt zur Homebase zu programmieren 
import utime
import math
import random
from microbit import *
from mbrobot import *

RobotContext.enableTrace(True)

winkel = []
winkel_rad = []
vektoren = []
fahrzeiten = []

def time_to_rad(time):
    degree = 360 / 2150 * time
    return math.radians(degree)

def home_vektor(vektor):
    a = vektor[0]
    b = vektor[1]
    distanz = math.sqrt(a ** 2 + b ** 2)
    alpha = math.atan2(a, b)
    alpha_strich = 180 - alpha
    drehzeit = int((215*alpha_strich)/36)
    
    return [drehzeit, distanz]
    


def polar_to_cart(vektoren):
    cartesianische_vektoren = []
      
    for v in vektoren:
        theta = time_to_rad(v[0])
        x = v[1] * math.cos(theta)
        y = v[1] * math.sin(theta)
        cartesianische_vektoren.append((x, y))
    
    return cartesianische_vektoren


def summen_vektor(vektoren):
    x = 0
    y = 0
    
    for vektor in vektoren:
        x = x + vektor[0]
        y = y + vektor[1]
        
    return [x, y]

def drehung():
    start_drehung = utime.ticks_ms()
    time = random.randrange(200,900,50)
    print(time)
    direction = random.choice([1,-1])
    if direction == -1:
        left()
        delay(time)
        stop()
    else:
        right()
        delay(time)
        stop()
        
    ende_drehung = utime.ticks_ms()
    dauer_drehung = utime.ticks_diff(ende_drehung,start_drehung)
    if direction == 1:
        entry = time
    else:
        entry = -1 * time
            
    winkel.append(entry)
    winkel_rad.append(time_to_rad(entry))

    
    
def geradeausfahrt():
    start_time = utime.ticks_ms()  # Startzeit in Millisekunden
    duration = 60 * 1000  # Dauer in Millisekunden (1 Minute)
    
    start_forward = utime.ticks_ms()
    forward()
    while True:
        # Prüfen, ob die Fahrtzeit abgelaufen ist
        if utime.ticks_diff(utime.ticks_ms(), start_time) >= duration:
            break

        # Kontinuierliche Distanzmessung
        d = getDistance()
        if d < 5:
            ende_forward = utime.ticks_ms()
            dauer_forward = utime.ticks_diff(ende_forward,start_forward)
            fahrzeiten.append(dauer_forward - 500)
            vektoren.append([winkel[-1], fahrzeiten[-1]])
            
            zuruecksetzen()
            drehung()
            
            start_forward = utime.ticks_ms()
            forward()
        
        # Fügen Sie eine kleine Verzögerung ein, um den Prozessor nicht zu überlasten
        utime.sleep_ms(100)
    
    # Anhalten des Roboters nach 1 Minute
    stop()
    
def ausrichtung(winkel):
    drehwinkel = sum(winkel)
    print(drehwinkel)
    
    if drehwinkel < 0:
        right()
        delay(abs(drehwinkel))
        stop()
    else:
        left()
        delay(abs(drehwinkel))
        stop()
        

def heimreise(vektor):
    drehzeit = -1 * vektor[0]
    fahrstrecke = int(vektor[1])
    
    if drehzeit >= 0:
        right()
        delay(drehzeit)
        stop()
        
    else:
        left()
        delay(abs(drehzeit))
        stop()
        
        
    forward()
    delay(fahrstrecke)
    stop()



drehung()

stop()

forward()
delay(1000)
fahrzeiten.append(1000)
vektoren.append([winkel[-1], fahrzeiten[-1]])
stop()
drehung()
stop()

forward()
delay(1500)
fahrzeiten.append(1500)
vektoren.append([winkel[-1], fahrzeiten[-1]])
print("Vektoren: ", vektoren)
stop()

print("Winkelliste: ", winkel)

ausrichtung(winkel)

c_vektoren = polar_to_cart(vektoren)

print("cartesianische Vektoren ", c_vektoren)

total = summen_vektor(c_vektoren)
print("Summenvektor: ", total)

r_vektor = home_vektor(total)

print("Home Vektor: ", r_vektor)

heimreise(r_vektor)



