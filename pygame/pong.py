import pygame
from klassenPong import Spieler

#Attribute
FENSTERBREITE = 640
FENSTERHOEHE = 480
schlaegerhoehe = 60

punkteSp1 = 0
punkteSp2 = 0
AnzeigePunkteSp1 = 0
AnzeigePunkteSp2 = 0

# Farben
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS  = ( 255, 255, 255)

class Ball():
    def __init__(self, xPos, yPos, durchmesser, bewegung_x = 4, bewegung_y = 4):
        self.xPos = xPos
        self.yPos = yPos
        self.durchmesser = durchmesser
        self.bewegung_x = bewegung_x
        self.bewegung_y = bewegung_y

    def bewegen(self):
        if self.xPos > (FENSTERBREITE - 20) or self.xPos < 0:
            self.bewegung_x = self.bewegung_x * -1
        if self.yPos > (FENSTERHOEHE - 20) or self.yPos < 0:
            self.bewegung_y = self.bewegung_y * -1
        self.xPos += self.bewegung_x
        self.yPos += self.bewegung_y
        

    def xPosGeben(self):
        return self.xPos
    def yPosGeben(self):
        return self.yPos
    def umdrehen(self):
        self.bewegung_x = self.bewegung_x * -1



# initialisieren von pygame
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
pygame.font.init()
clock = pygame.time.Clock()
ball = Ball(10, 30, 20)
spieler1 = Spieler(20, 150, 0, 0)
spieler2 = Spieler(FENSTERBREITE - (2 * 20), 20, 0, 0)


# Fenster öffnen
screen.fill(WEISS)

# Titel für Fensterkopf
pygame.display.set_caption("Krasses Pong")


# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

#Gewinneranzeigen
def gewinnerAnzeigen(gewinner):
    screen.fill(SCHWARZ)
    schrift = pygame.font.SysFont('Arial', 35, True, False)
    text = schrift.render(gewinner, True, ROT)
    screen.blit(text, [150, 250])
    pygame.time.delay(2000)

def hintergrundErstellen():
    screen.fill(SCHWARZ)
    AnzeigePunkteSp1 = int(spieler1.punkteGeben()//3)
    text1 = "Punkte " + str(AnzeigePunkteSp1)
    AnzeigeSp1 = pygame.font.SysFont('Arial', 15, True, False)
    textSp1 = AnzeigeSp1.render(text1, True, ROT)
    screen.blit(textSp1, [10, 10])
    AnzeigePunkteSp2 = int(spieler2.punkteGeben()//3)
    AnzeigeSp2 = pygame.font.SysFont('Arial', 15, True, False)
    text2 = "Punkte " + str(AnzeigePunkteSp2)
    textSp2 = AnzeigeSp2.render(text2, True, ROT)
    screen.blit(textSp2, [FENSTERBREITE - 75, 10])

# Schleife Hauptprogramm
while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat das Spiel beendet")
        elif event.type == pygame.KEYDOWN:    
            #Hauptspiel Einstellungen 
            if event.key == pygame.K_q:
                spielaktiv = False
            
            #elif event.key == pygame.K_SPACE:
                
            # Taste für Spieler 1
            elif event.key == pygame.K_w:
                spieler1.bewegungSetzen(-6)

            elif event.key == pygame.K_s:
                spieler1.bewegungSetzen(+6)
                
            

            # Taste für Spieler 2
            elif event.key == pygame.K_UP:
                spieler2.bewegungSetzen(-6)
            elif event.key == pygame.K_DOWN:
                spieler2.bewegungSetzen(+6)
        
        #zum Stoppen der Spielerbewegung 
        if event.type == pygame.KEYUP:
            

            # Tasten für Spieler 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                spieler1.bewegungSetzen(0)
            
            # Tasten für Spieler 2
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spieler2.bewegungSetzen(0)



    # Spiellogik hier integrieren
    if spieler1.bewegungGeben() != 0:
        spieler1.yPosVerschieben(spieler1.bewegungGeben())

    if spieler1.yPosGeben() < 0:
        spieler1.yPosSetzen(0)

    if spieler1.yPosGeben() > FENSTERHOEHE - schlaegerhoehe:
        spieler1.yPosSetzen(FENSTERHOEHE - schlaegerhoehe)

    if spieler2.bewegungGeben() != 0:
        spieler2.yPosVerschieben(spieler2.bewegungGeben())

    if spieler2.yPosGeben() < 0:
        spieler2.yPosSetzen(0)

    if spieler2.yPosGeben() > FENSTERHOEHE - schlaegerhoehe:
        spieler2.yPosSetzen(FENSTERHOEHE - schlaegerhoehe)

    if spieler2.xPosGeben() < (ball.xPosGeben() + 20) and spieler2.yPosGeben() < ball.yPosGeben() and (spieler2.yPosGeben() + 60) > ball.yPosGeben():
        ball.umdrehen()

    if (spieler1.xPosGeben() + 20) > ball.xPosGeben() and spieler1.yPosGeben() < ball.yPosGeben() and (spieler1.yPosGeben() + 60) > ball.yPosGeben():
        ball.umdrehen()


    
    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
    hintergrundErstellen()
    #Ball
    ball.bewegen()
    pygame.draw.ellipse(screen, WEISS, [ball.xPosGeben(),ball.yPosGeben(), 20, 20])
    # -- Spielerfigur 1
    pygame.draw.rect(screen, WEISS, [spieler1.xPosGeben(), spieler1.yPosGeben(), 20, schlaegerhoehe])
    # -- Spielerfigur 2
    pygame.draw.rect(screen, WEISS, [spieler2.xPosGeben(), spieler2.yPosGeben(), 20, schlaegerhoehe])
    if ball.xPosGeben() < 5:
        gewinnerAnzeigen("Spieler 2 hat gewonnen")
        spieler2.punkteErhöhen()

    elif ball.xPosGeben() > (FENSTERBREITE -25):
        gewinnerAnzeigen("Spieler 1 hat gewonnen")
        spieler1.punkteErhöhen()


    #  Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)


pygame.quit()