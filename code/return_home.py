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
journal = [[0, "Drehung"]]

def log_bewegung(ereignis):
    timestamp = utime.ticks_ms()
    eintrag = [timestamp, ereignis]
    bewegungs_log.append(eintrag)

def ausfahrt():
    time = random.randrange(500,2000,500)
    #log_bewegung("Beginn forward")
    start_ausfahrt = utime.ticks_ms()
    forward()
    delay(time)
    #log_bewegung("Ende forward")
    ende_ausfahrt = utime.ticks_ms()
    dauer_ausfahrt = utime.ticks_diff(ende_ausfahrt,start_ausfahrt)
    stop()
    entry = [dauer_ausfahrt, "Geradeaus"]
    journal.append(entry)

def drehung():
    #log_bewegung("Beginn Drehung")
    start_drehung = utime.ticks_ms()
    time = random.randrange(200,900,50)
    direction = random.choice([1,-1])
    if direction == 1:
        left()
        delay(time)
        stop()
    else:
        right()
        delay(time)
        stop()
        
    #log_bewegung("Ende Drehung")
    ende_drehung = utime.ticks_ms()
    dauer_drehung = utime.ticks_diff(ende_drehung,start_drehung)
    if direction == 1:
        entry = [dauer_drehung, "Drehung"]
    else:
        entry = [-1 * dauer_drehung, "Drehung"]
            
    journal.append(entry)

def zuruecksetzen():
    #log_bewegung("Beginn backward")
    start_rueckfahrt = utime.ticks_ms()
    backward()
    delay(500)
    #log_bewegung("Ende backward")
    stop()
    ende_rueckfahrt = utime.ticks_ms()
    dauer_rueckfahrt = utime.ticks_diff(ende_rueckfahrt,start_rueckfahrt)
    entry = [dauer_rueckfahrt, "Rueckfahrt"]
    

def geradeausfahrt():
    start_time = utime.ticks_ms()  # Startzeit in Millisekunden
    duration = 60 * 1000  # Dauer in Millisekunden (1 Minute)
    
    start_forward = utime.ticks_ms()
    forward()
    #log_bewegung("forward")
    while True:
        # Prüfen, ob die Fahrtzeit abgelaufen ist
        if utime.ticks_diff(utime.ticks_ms(), start_time) >= duration:
            break

        # Kontinuierliche Distanzmessung
        d = getDistance()
        if d < 5:
            ende_forward = utime.ticks_ms()
            dauer_forward = utime.ticks_diff(ende_forward,start_forward)
            entry = [dauer_forward, "Geradeaus"]
            journal.append(entry)
            zuruecksetzen()
            drehung()
            
            start_forward = utime.ticks_ms()
            forward()
            #log_bewegung("forward")
        
        # Fügen Sie eine kleine Verzögerung ein, um den Prozessor nicht zu überlasten
        utime.sleep_ms(100)
    
    # Anhalten des Roboters nach 1 Minute
    stop()
    
def polar_vektoren(journal):
    for entry in journal:
        if entry[1] == "Drehung":
            tmp = entry[0]
            entry[0] = time_to_rad(tmp)
            
    vektoren = []
    count = len(journal)// 2 + 2
    for i in range(0,count,2):
        v = (journal[i][0],journal[i+1][0])
        vektoren.append(v)
    return vektoren

def drehwinkel_total(p_vektoren):
    winkel = 0
    for v in p_vektoren:
        winkel = winkel + v[0]
    return winkel

def polar_to_cart(vektoren):
    cartesianische_vektoren = []
    
    for v in vektoren:
        x = v[1] * math.cos(v[0])
        y = v[1] * math.sin(v[0])
        cartesianische_vektoren.append((x, y))
    
    return cartesianische_vektoren

def heim_vektor(vektoren):
    x = 0
    y = 0
    for v in vektoren:
        x = x + v[0]
        y = y + v[1]
    
    return (-1*x, -1*y)

def cart_to_polar(vektor):
    x = vektor[0]
    y = vektor[1]
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(x, y)
    degree = math.degrees(theta)
    drehzeit = (215*degree)/36
    return (drehzeit, r)

def ausrichten(drehwinkel):
    degree = math.degrees(drehwinkel)
    drehzeit = int(abs((215*degree)/36))
    if drehwinkel < 0:
        left()
        delay(drehzeit)
        stop()
    else:
        right()
        delay(drehzeit)
        stop()
        
def nach_hause(anweisungs_vektor):
    drehzeit = int(anweisungs_vektor[0])
    fahrzeit = int(anweisungs_vektor[1])
    
    if drehzeit < 0:
        right()
        delay(abs(drehzeit))
        stop()
    else:
        left()
        delay(drehzeit)
        stop()
    
    forward()
    delay(fahrzeit)
    stop()
        
    

ausfahrt()
drehung()
start_forward = utime.ticks_ms()
forward()
delay(2000)
ende_forward = utime.ticks_ms()
dauer_forward = utime.ticks_diff(ende_forward,start_forward)
entry = [dauer_forward, "Geradeaus"]
journal.append(entry)
stop()
drehung()
start_forward = utime.ticks_ms()
forward()
delay(2000)
ende_forward = utime.ticks_ms()
dauer_forward = utime.ticks_diff(ende_forward,start_forward)
entry = [dauer_forward, "Geradeaus"]
journal.append(entry)
stop()
print("Journal ",journal)
p_vektoren = polar_vektoren(journal)
print("Polarvektoren ", p_vektoren)
c_vektoren = polar_to_cart(p_vektoren)
drehwinkel= drehwinkel_total(p_vektoren)
print("Drehwinkel: ", drehwinkel)
print("Cartesianische Vektoren: ", c_vektoren)
nach_hause_vektor = heim_vektor(c_vektoren)
print("Nach Hause Vektor ",nach_hause_vektor)
anweisung = cart_to_polar(nach_hause_vektor)
print("Anweisungsvektor: ", anweisung)
ausrichten(drehwinkel)

#nach_hause(anweisung)





