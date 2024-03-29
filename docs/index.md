---
header-includes:
    - \usepackage[german]{babel}
---

# Einführung in die Programmierung eines Maqueen-Roboters

In dieser Unterrichtseinheit sollen die Schülerinnen und Schüler (SuS)
in die Besonderheiten der Programmierung eines Roboters eingeführt
werden. Der Maqueen-Roboter soll dabei als Modell eines
Roboter-Staubsaugers dienen. Damit ein Roboter-Staubsauger ein Zimmer
staubfrei halten kann, muss er nicht nur staubsaugen, sondern die
gesamte Fläche des Zimmers abfahren und rechtzeitig zum Leeren des
Staubbehälters bzw. zum Aufladen des Akkus wieder zur Basisstation
zurückkehren. Daraus ergeben sich verschiedene
Probleme bezüglich der Steuerung des Roboter-Staubsaugers.

## Lernziele  

Die SuS sollen in dieser Unterrichtseinheit in die Lage versetzt werden 

- die Unterschiede zwischen Ablauf- und Zustandsdiagrammen zu erläutern;
- Anforderungen an einen Roboter in einem UML-Zustandsdiagramm darzustellen;
- einfache Bewegungsabläufe eines Roboters unter Einbezug der zur
  Verfügung stehenden Sensoren zu programmieren sowie
- konkrete Programmentwürfe durch Tests mit einem Maqueen-Roboter zu überprüfen.

Differenzierungen der Aufgabenstellungen sind insbesondere im zweiten und dritten
Lernziel möglich.

Im zweiten Lernziel ist es möglich, dass die schwächeren SuS sich auf
das Lesen und Verstehen eines Zustandsdiagramms beschränken. Um einen
Roboter programmieren zu können, ist es nicht erforderlich, dass die
Problemstellung selbständig in einem Zustandsdiagramm abgebildet werden
kann.

Im dritten Lernziel kann das Gros der Klasse sich darauf beschränken,
den Roboter-Staubsauger so zu programmieren, dass er Hindernissen
ausweicht und einen grossen Teil der Raumfläche abdeckt.  
Talentiertere SuS können die Steuerung dahingehend ergänzen, dass sie einen
Algorithmus entwerfen und implementieren, der den Maqueen-Roboter nach
einer bestimmten Zeit anhalten lässt. Wirklich talentierte SuS können das
Programm noch um eine Rückfahr-Funktion ergänzen, welche den
Maqueen-Roboter wieder an den Ausgangspunkt zurückfahren lässt. Dies
erfordert jedoch ein gewisses Mass an Kenntnissen aus der
Vektorgeometrie. 

## Ablauf

Der Unterricht gliedert sich in vier Phasen:

1. Einführung in die zustandsbasierte Programmierung
2. Einführung in die Übertragung von Programmen auf den Maqueen-Roboter 
3. Analyse und Darstellung der Steuerungsproblematik eines
   Roboter-Staubsaugers
4. Programmierung der Steuerung des Maqueen-Roboters  

### Einführung in die zustandsbasierte Programmierung

Damit die SuS ein Verständnis für die Funktion und die Darstellung von
Zustandsdiagrammen entwickeln können, wird das Beispiel aus dem
Lehrmittel Arnold/ Donner/ Hauser/ Hauswirth/ Hromkovič/ Kohn/ Komm/
Maletinsky/ Roth, Informatik: Programmieren und Robotik: Grundlagen
der Informatik für Schweizer Maturitätsschulen, 1. Auflage, Baar 2021, Klett
und Balmer Verlag, Seite 142 (Beispiel 8.1, Ampelsteuerung),
aufgenommen.

Die SuS sollen ihre Schullaufbahn als UML-Zustandsdiagramm darstellen
können. Die entsprechenden Erläuterungen sind in einem
[separaten Text](kbw_laufbahn.md) 
zusammengestellt. In diesem Beispiel wird auch der
UML-Darstellungsstandard für Zustandsdiagramme eingeführt.

Für die Einführung, wie die Programme der SuS auf den Maqueen Roboter übertragen
werden, wird auf die Anleitung im Lehrmittel Arnold et al., Seite 143 f.,
verwiesen.

### Analyse und Darstellung der Steuerungsproblematik eines Roboter-Staubsaugers

Der Roboter-Staubsauger soll seine Basisstation verlassen und nach einer
zufällig gewählten Strecke in einem ebenfalls zufällig gewählten Winkel
abdrehen und dann geradeaus fahren, bis er auf ein Hindernis trifft.
Sobald der Roboter-Staubsauger auf ein Hindernis trifft, soll er
zurücksetzen und in einem zufällig gewählten Winkel abdrehen und wieder
so lange geradeaus fahren, bis er neuerdings auf ein Hindernis trifft.

Im folgenden Zustandsdiagramm sind die einzelnen Elemente dargestellt. Die
Farben entsprechen den Schwierigkeitsgraden von Skipisten. Die blauen Elemente
sollten dabei von allen SuS bewältigt werden können.

<img src="../visualisierungen/detailliertes_zustandsdiagramm.svg">

### Aufträge an die Schülerinnen und Schüler

Die obigen Überlegungen führen zu Aufträgen an die SuS, die in einem 
[separaten Text](auftraege.md) zusammengestellt werden.

### Musterlösung

Die Musterlösung wurde lediglich für die für alle SuS zu bewältigende Aufgabe
sowie für den Timer verfasst. Damit dürfte man sich bereits am oberen
Ende dessen befinden, was in vier Lektionen zu bewältigen ist. Die
Implementierung einer Funktion für die Rückfahrt zur Basisstation würden
den Rahmen einer vierstündigen Unterrichtseinheit bei Weitem sprengen
und ist deshalb nicht implementiert.

Der Code der Musterlösung findet sich
[in der Datei `steuerung_einfach.py` (Grundauftrag)](../code/steuerung_einfach.py) 
sowie
[in der Datei `steuerung_mit_timer.py` (mit Timer)](../code/steureung_mit_timer.py).
