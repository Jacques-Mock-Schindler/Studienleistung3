# Einführung in die Programmierung eines Maqueen-Roboters

In dieser Unterrichtseinheit sollen die Schülerinnen und Schüler (SuS)
in die Besonderheiten der Programmierung eines Roboters eingeführt
werden. Der Maqueen-Roboter soll dabei als Modell eines
Roboter-Staubsaugers dienen. Damit ein Roboter-Staubsauger ein Zimmer
staubfrei halten kann, muss er nicht nur staubsaugen, sondern die
gesamte Fläche des Zimmers abfahren. Daraus ergeben sich verschiedene
Probleme bezüglich der Steuerung des Roboter-Staubsaugers.

## Lernziele

Die SuS sollen in dieser Unterrichtseinheit in die Lage versetzt werden 

- die Unterschiede zwischen Ablauf- und Zustandsdiagrammen zu erläutern;
- Anforderungen an einen Roboter in einem UML-Zustandsdiagramm darzustellen;
- einfache Bewegungsabläufe eines Roboters unter Einbezug der zur
  Verfügung stehenden Sensoren zu programmieren sowie
- konkrete Programmentwürfe durch Tests mit einem Maqueen-Roboter zu überprüfen.

Differenzierungen der Lernziele sind insbesondere im zweiten und dritten
Lernziel möglich.

Im zweiten Lernziel ist es möglich, dass die schwächeren SuS sich auf
das Lesen und Verstehen eines Zustandsdiagramms beschränken. Um einen
Roboter programmieren zu können ist es nicht erforderlich, dass die
Problemstellung selbständig in einem Zustandsdiagramm abgebildet werden
kann.

Im dritten Lernziel kann das Gros der Klasse sich auf das hin und her
Fahren zwischen zwei Hindernissen (Wänden) beschränken. Stärkere SuS
können die Steuerung dahingehend ergänzen, dass sie einen Algorithmus
entwerfen und implementieren, der den Maqueen-Roboter die ganze
Zimmerfläche abfahren lässt und nach einer festgelegten Zeit zurück zur
Basisstation fährt.

## Ablauf

Der Unterricht gliedert sich in drei Phasen:

1. Einführung in die zustandsbasierte Programmierung
2. Analyse und Darstellung der Steuerungsproblematik eines
   Roboter-Staubsaugers  
3. Programmierung der Steuerung des Maqueen-Roboters  

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

### Analyse und Darstellung der Steuerungsproblematik eines Roboter-Staubsaugers

Der Roboter-Staubsauger soll seine Basisstation verlassen und nach einer
zufällig gewählten Strecke in einem ebenfalls zufällig ewählten Winkel
abdrehen und dann geradeaus fahren, bis er auf ein Hinderniss trifft.
Sobald der Roboter-Staubsauger auf ein Hindreniss trifft, soll er
zurücksetzen und in einem zufällig gewählten Winkel abdrehen und wieder
so lange gerade aus fahren, bis er neuerdings auf ein Hindernis trifft.

Dieser Vorgang soll während einer vorgebenen Zeit wiederholt werden.

Leistungsstarke SuS können sich zusätzlich noch mit der Frage
auseinandersetzen, wie die Steuerung ergänzt werden muss, damit der
Roboter-Staubsauger nach Ablauf der vorgebenen Zeit das Abfahren der
Zimmerfläche einstellt und  wieder zurück zur Basisstation findet.

Im folgenden Zustandsdiagramm sind die einzelnen Elemente dargestellt. Die
Farben entsprechen den Schwierigkeitsgraden von Skipisten. Die blauen Pisten
sollten dabei von allen SuS bewältigt werden können.

![Detailliertes
Zustandsdiagramm](../visualisierungen/detailliertes_zustandsdiagramm.svg)

### Aufträge an die Schülerinnen und Schüler

Die obigen Überlegungen führen zu Aufträgen an die SuS, die in einem spearaten
Text zusammengestellt werden.
