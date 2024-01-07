# Die Darstellung der Laufbahn eines Absolventen der KBW als Zustandsdiagramm

Die Laufbahn einer Schülerin bzw. eines Schülers (SuS) an der
Kantonsschule Büelrain kann als
[UML-Zustandsdiagramm](https://de.wikipedia.org/wiki/Zustandsdiagramm_(UML))
grafisch dargestellt werden.

## Darstellungselemente für ein UML Zustandsdiagramm

Für Zustandsdiagramme gelten die folgenden grafischen Standards:

- Zustände werden als Rechtecke mit abgerundeten Ecken dargestellt.
  
  ![Zustand](../visualisierungen/zustand.svg)

- Übergänge von einem Zustand in einen anderen Zustand werden als Pfeile
  mit Beschriftung dargestellt.

  ![Übergang](../visualisierungen/uebergang.svg)

- Der Start wird mit einem ausgefüllten schwarzen Punkt dargestellt.
- Das Ende wird mit einem von einem Ring umgebenen schwarzen Punkt
  dargestellt.

  ![Endzustand](../visualisierungen/endzustand.svg)

- Verzweigungen bzw. Vereinigungen werden durch einen dicken schwarzen
  Strich dargestellt.

  ![Verzweigung](../visualisierungen/verzweigung.svg)

  ![Vereinigung](../visualisierungen/vereinigung.svg)

## Die KBW Laufbahn

Um die Laufbahn an der KBW als UML-Zustandsdiagramm darstellen zu
können, muss man sich Schritt für Schritt die verschiedenen Phasen,
welche, eine Schülerin oder ein Schüler durchläuft, als separate
Zustände vorstellen.

Die Laufbahn an der KBW beginnt mit der Anmeldung zur Aufnahmeprüfung.
Damit man sich anmelden kann, muss allerdings das Anmeldefenster für die
Aufnahmeprüfung bereit sein. Dies wird mit einem Startzustand
dargestellt.

![Anmeldefenster offen](../visualisierungen/anmeldefenster.svg)

Allerdings ist man erst nach dem Bezahlen der Anmeldegebühr wirklich
angemeldet. Wird die Anmeldegebühr nicht bezahlt, ist die Laufbahn
beendet, bevor sie wirklich begonnen hat.

![Nicht bezahlte Anmeldegebühr](../visualisierungen/anmeldegebuehr.svg)

Nach der Anmeldung muss die Aufnahmeprüfung bestanden werden. Wenn dies
der Fall ist, ist man an die KBW aufgenommen.

![Aufnahme an die KBW](../visualisierungen/aufnahme.svg)