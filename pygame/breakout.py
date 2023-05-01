# Importieren der Pygame-Bibliothek
import pygame, sys, time, random
from pygame.locals import *

# Variablen
MULTIPLIKATOR = 20
mauersteine = 0

# genutzte Farben
ORANGE  = ( 255, 140,   0)
SCHWARZ = (   0,   0,   0)
WEISS   = ( 255, 255, 255)

#Eigenschaften des Balls
ball_x = random.randint(3,16)
ball_y = 23
ball_x_richtung = 1
ball_y_richtung = -1
ball_x_alt = 0
ball_y_alt = 0

#Eigenschaften des Spielers
spielfigur_x = 0
spielfigur_y = 27
spielfigur_bewegung = 0
spielfigur_x_alt = 0

def element_zeichnen(spalte,reihe):
    pygame.draw.rect(fenster, ORANGE,(spalte*MULTIPLIKATOR, reihe*MULTIPLIKATOR,MULTIPLIKATOR,MULTIPLIKATOR)) 

def probe_elemente_zeichnen():
    element_zeichnen(0,1)
    element_zeichnen(0,2)
    element_zeichnen(0,3)
    element_zeichnen(0,4)

# Spielfeld erzeugen über Berechnung
fenster = pygame.display.set_mode((20 * MULTIPLIKATOR, 30 * MULTIPLIKATOR))

# Hintergrundfarbe Fenster
fenster.fill(WEISS)

# Titel für Fensterkopf
pygame.display.set_caption("Breakout in Python")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

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
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
] 

def kor(zahl):
    zahl = zahl * MULTIPLIKATOR
    return zahl

# Spielelement zeichnen
def element_zeichnen(spalte,reihe):
    pygame.draw.rect(fenster, ORANGE, [kor(spalte)+1, kor(reihe)+1,kor(1)-1,kor(1)-1])

# Spielelement löschen
def element_löschen(spalte, reihe):
    pygame.draw.rect(fenster, WEISS, [kor(spalte), kor(reihe),kor(1),kor(1)])

def ball_zeichnen(x,y):
    pygame.draw.ellipse(fenster, SCHWARZ, [kor(x),kor(y),kor(1),kor(1)],0)

def spielfigur_zeichnen(x):
    pygame.draw.rect(fenster, SCHWARZ,(kor(x), kor(spielfigur_y),50,kor(1)))

def spielfigur_loeschen(x):
    pygame.draw.rect(fenster, WEISS,(kor(x), kor(spielfigur_y),50,kor(1)))

def mauersteineZählen():
    global mauersteine
    global karte
    for i in range(len(karte)):
        for j in range(len(karte[i])):
            if karte[i][j] == 1:
                mauersteine += 1

def prüfe_gewonnen():
    global mauersteine
    global ball_x_richtung
    global ball_y_richtung   
    if mauersteine > 0:
        print("Es gibt noch ", mauersteine)
    else:
        ball_x_richtung = 0
        ball_y_richtung = 0
        print("Glückwunsch du hast gewonnen")


# Blöcke einzeichnen
for x in range(0,20):
    for y in range(0,27):
        if karte[y][x] != 0:
            element_zeichnen(x,y)

# Kollisionskontrolle mit Blöcken
def kollisionskontrolle_mit_Mauer():
    global mauersteine
    global ball_y_richtung
    global ball_x_richtung
    if ball_y_richtung == -1:
        if karte[ball_y - 1][ball_x] == 1:
            karte[ball_y - 1][ball_x] = 0
            element_löschen(ball_x, ball_y - 1)
            ball_y_richtung = 1
            print("trifft Mauerstein oberhalb")
            mauersteine -= 1
        else:
            if ball_x_richtung == 1:
                if ball_x <= 17:
                    if karte[ball_y - 1][ball_x + 1] != 0:
                        karte[ball_y - 1][ball_x + 1] = 0 
                        element_löschen(ball_x + 1, ball_y - 1)
                        ball_y_richtung = 1
                        print("trifft Mauerstein rechts oberhalb")
                        ball_x_richtung = -1
                        mauersteine -= 1
            else:  
                if ball_x >= 1 :
                    if karte[ball_y - 1][ball_x - 1] != 0:
                        karte[ball_y - 1][ball_x - 1] = 0
                        element_löschen(ball_x - 1, ball_y - 1)
                        ball_y_richtung = 1
                        print("trifft Mauerstein links oberhalb")
                        ball_x_richtung = 1
                        mauersteine -= 1
#Init
mauersteineZählen()
# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            spielaktiv = False
            print("Spieler hat beendet")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spielfigur_bewegung = 1
            if event.key == pygame.K_LEFT:
                spielfigur_bewegung = -1

    if (spielfigur_x == 0 and spielfigur_bewegung == -1):
        spielfigur_bewegung = 0

    if spielfigur_x == 18 and spielfigur_bewegung == 1:
        spielfigur_bewegung = 0

    if ball_x >= 19:
        ball_x_richtung = -1
    if ball_x <= 0:
        ball_x_richtung = 1
    if ball_y == 29:
        ball_y_richtung = -1
    if ball_y == 0:
        ball_y_richtung = 1

    
    ball_x_alt = ball_x
    ball_y_alt = ball_y
    ball_x += ball_x_richtung
    ball_y += ball_y_richtung
    
    spielfigur_x_alt = spielfigur_x
    spielfigur_x += spielfigur_bewegung
    
    element_löschen(ball_x_alt, ball_y_alt)
    ball_zeichnen(ball_x, ball_y)
    spielfigur_loeschen(spielfigur_x_alt)
    spielfigur_zeichnen(spielfigur_x)
    spielfigur_1_bewegung = 0
    
    kollisionskontrolle_mit_Mauer()

    
    prüfe_gewonnen()
    # Fenster aktualisieren
    pygame.display.flip()


    # Refresh-Zeiten festlegen
    clock.tick(10)

pygame.quit()