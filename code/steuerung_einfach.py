import random
from microbit import * 
from mbrobot import *

def ausfahrt():
    """
    Die Funktion steuert die Ausfahrt aus der Basistation des
    Roboter-Staubsaugers.  
    Mit time = random.randrange(500,2000,500) wird sichergestellt, dass
    der Roboterstaubsauger nicht bei jeder Ausfahrt an der selben Stelle
    ablenkt.
    """

    time = random.randrange(500,2000,500)
    forward()
    delay(time)
    stop()

def drehung():
    """
    Die Funktion steuert die Ablenkungen nach der Ausfahrt oder um einem
    Hindernis auszuweichen. Der Abrehwinkel wird dabei zufällig
    festgelegt.  
    Mit time = random.randrange(200,1100,50) wird der Winkel zwischen ca
    30 und 90 Grad festgelegt.
    Mit direction = random.choice([1,-1]) wird die Drehrichtung zufällig
    auf links und rechts verteilt.
    """
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
    """
    Die Funktion zurücksetzen lässt den Roboter-Staubsauger während
    einer halben Sekunde zurückfahren. Die Funktion wird verwendet, wenn
    der Roboter-Staubsauger auf ein Hindernis trifft.
    """
    backward()
    delay(500)
    stop()

def geradeausfahrt():
    """
    Die Funktion steuert den Roboter-Staubsauger auf der Fläche. Mit
    repeat: wird sichergestellt, dass der Distanzsensor permanent den
    Abstand zum nächsten Hindernis misst. Sobald diese Distanz unter 5cm
    fällt, setzt der Roboter-Staubsauger zurück, dreht ab und fährt dann
    weiter.  
    Die Funktion ist damit, dass sie sich selber aufruft ein Beispiel
    für das Konzept der Rekursion.
    """
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












