# Importieren der Pygame-Bibliothek
import pygame, sys, time, random
from pygame.locals import *
from klassenBreakout import * 

# unser Multiplikator 
MULTIPLIKATOR = 20

# Spielfeld erzeugen über Berechnung
fenster = pygame.display.set_mode((20 * MULTIPLIKATOR, 30 * MULTIPLIKATOR))

# Titel für Fensterkopf
pygame.display.set_caption("Breakout in Python")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()
pygame.key.set_repeat(10,0)

# genutzte Farben
ORANGE  = ( 255, 140,   0)
SCHWARZ = (   0,   0,   0)
WEISS   = ( 255, 255, 255)

# Spielfeld mit Mauersteinen 
karte=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


# Spielball Variablen
ball_x = random.randint(3,16)
ball_y = 19
ball_x_richtung = 1
ball_y_richtung = 1
ball_x_alt = 0
ball_y_alt = 0

# Spielerfigur
spielfigur_1_x = 10
spielfigur_1_y = 28
spielfigur_1_bewegung = 0

# Hintergrundfarbe Fenster
fenster.fill(WEISS)

# Korrekturfaktor berechnen
def kor(zahl):
    zahl = zahl * MULTIPLIKATOR
    return zahl

# Spielelement zeichnen
def element_zeichnen(spalte,reihe):
    pygame.draw.rect(fenster, ORANGE, [kor(spalte)+1, kor(reihe)+1,kor(1)-1,kor(1)-1])

def element_loeschen(spalte,reihe):
    pygame.draw.rect(fenster, WEISS, [kor(spalte), kor(reihe),kor(1),kor(1)])

def ball_zeichnen(x,y):
    pygame.draw.ellipse(fenster, SCHWARZ, [kor(x), kor(y),kor(1), kor(1)], 0)

def spielfigur_zeichnen(x):
    pygame.draw.rect(fenster, SCHWARZ,(kor(x), kor(spielfigur_1_y),50,kor(1)))

def spielfigur_loeschen(x):
    pygame.draw.rect(fenster, WEISS,(kor(x), kor(spielfigur_1_y),50,kor(1)))

# Ausgabe Mauersteine im Spielfenster
for x in range(0,20):
    for y in range(0,27):
        if karte[y][x] != 0:
            element_zeichnen(x,y)


ball_x = random.randint(3,16)
ball_y = 19
ball_x_richtung = 1
ball_y_richtung = 1
ball_x_alt = 0
ball_y_alt = 0

ball = Ball(random.randint(3,16),19,1,1,0,0)
ball_zeichnen(ball.get_xPos(), ball.get_yPos())

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat beendet")

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     naechsterschritt = True
        #     print("Nächster Schritt")

        if event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
                spielfigur_1_bewegung = -1
            elif event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
                spielfigur_1_bewegung = 1            

    # Spiellogik
    # -- Spielfigur darf das Spielfeld links nicht verlassen
    if (spielfigur_1_x == 0 and spielfigur_1_bewegung == -1):
        spielfigur_1_bewegung = 0

    if spielfigur_1_x == 18 and spielfigur_1_bewegung == 1:
        spielfigur_1_bewegung = 0

    # Ballbewegung
    if ball.get_xPos() <= 0:
        ball.set_xRichtung(1)
    if ball.get_xPos() >= 19:
        ball.set_xRichtung(-1)
    if ball.get_yPos()  <= 0:
        ball.set_yRichtung(1)
    if ball.get_yPos()  > 29:
        # ball_y_richtung = -1
        ball.set_xRichtung(0)
        ball.set_yRichtung(0)
        print("Verloren :(")

    # Spielfigurbewegung
    spielfigur_1_x_alt = spielfigur_1_x
    spielfigur_1_x += spielfigur_1_bewegung

    # Ball trifft Mauerstein
    # Kontrolle auf möglich Kollision
    if ball.get_yRichtung() == -1:
        # Ball ist in Aufwärtsbewegung
        # genau darüber ein Mauerstein?
        if karte[ball.get_yPos()-1][ball.get_xPos()] != 0:
            print("trifft Mauerstein oberhalb")
            # Mauerstein wird gelöscht vom Bildschirm
            element_loeschen(ball.get_xPos(), ball.get_yPos()-1)
            # Mauerstein wird gelöscht aus der Liste karte
            karte[ball.get_yPos()-1][ball.get_xPos()] = 0
            ball.set_yRichtung(1)
        else:
            if ball.get_xRichtung() == 1:
                # Ball bewegt sich nach rechts
                if karte[ball.get_yPos()-1][ball.get_xPos()+1] != 0:
                    print("trifft Mauerstein rechts oberhalb")
                    # Mauerstein wird gelöscht vom Bildschirm
                    element_loeschen(ball.get_xPos()+1, ball.get_yPos()-1)
                    # Mauerstein wird gelöscht aus der Liste karte
                    karte[ball.get_yPos()-1][ball.get_xPos()+1] = 0
                    ball.set_yRichtung(1)
                    # trifft auf Ecke, also gleich Richtung zurück
                    ball.set_xRichtung(-1)
            else:
                # Ball bewegt sich nach links
                if karte[ball.get_yPos()-1][ball.get_xPos()-1] != 0:
                    print("trifft Mauerstein links oberhalb")
                    # Mauerstein wird gelöscht vom Bildschirm
                    element_loeschen(ball.get_xPos()-1, ball.get_yPos()-1)
                    # Mauerstein wird gelöscht aus der Liste karte
                    karte[ball.get_yPos()-1][ball.get_xPos()-1] = 0
                    ball.set_yRichtung(1)
                    # trifft auf Ecke, also gleich Richtung zurück
                    ball.set_xRichtung(1)

    # Ball trifft Schläger
    # Kontrolle auf möglich Kollision
    if ball.get_yPos() == 27 and ball.get_yRichtung() == 1:
        print("Kontrolle auf Kollision mit Schläger")

        # Ball kommt von links:
        if ball.get_xRichtung() == 1:
            print("Ball kommt von links")
            if ball.get_xPos()+1 >= spielfigur_1_x and ball.get_xPos()+1 <= spielfigur_1_x+3:
                print("Ball trifft Schläger")
                ball.set_yRichtung(-1)

        # Ball kommt von rechts:
        if ball.get_xRichtung() == -1:
            print("Ball kommt von rechts")
            if ball.get_xPos()-1 >= spielfigur_1_x and ball.get_xPos()-1 <= spielfigur_1_x+3:
                print("Ball trifft Schläger")
                ball.set_yRichtung(-1)

    # Siegbedingung erfüllt?
    mauersteine = 0
    for i in range(len(karte)):
        for j in range(len(karte[i])):
            if karte[i][j] == 1:
                mauersteine = mauersteine + 1
    if mauersteine == 0:
            
            ball.set_xRichtung(0)
            ball.set_yRichtung(0)
            print("Gewonnen - herzlichen Glückwunsch")

    ball.set_xAlt(ball.get_xPos())
    ball.set_yAlt(ball.get_yPos())
    ball.set_xPos(ball.get_xPos() + ball.get_xRichtung())
    ball.set_yPos(ball.get_yPos() + ball.get_yRichtung())

    # Ball zeichnen
    element_loeschen(ball.get_xAlt(), ball.get_yAlt())
    ball_zeichnen(ball.get_xPos(), ball.get_yPos())

    # Spielerfigur zeichnen
    spielfigur_loeschen(spielfigur_1_x_alt)
    spielfigur_zeichnen(spielfigur_1_x)
    spielfigur_1_bewegung = 0

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(10)

pygame.quit()

exit()