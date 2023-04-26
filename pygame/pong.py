import pygame

#Attribute
FENSTERBREITE = 640
FENSTERHOEHE = 480

spielfigur_1_x = 20
spielfigur_1_y = 150
spielfigur_1_bewegung = 0
spielfigur_2_x = FENSTERBREITE - (2 * 20)
spielfigur_2_y = 20
spielfigur_2_bewegung = 0
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
        pygame.draw.ellipse(screen, WEISS, [self.xPos, self.yPos, 20, 20])

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


# Fenster öffnen
screen.fill(WEISS)

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")


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
    AnzeigePunkteSp1 = int(punkteSp1//3)
    text1 = "Punkte " + str(AnzeigePunkteSp1)
    AnzeigeSp1 = pygame.font.SysFont('Arial', 15, True, False)
    textSp1 = AnzeigeSp1.render(text1, True, ROT)
    screen.blit(textSp1, [10, 10])
    AnzeigePunkteSp2 = int(punkteSp2//3)
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
                spielfigur_1_bewegung = -6

            elif event.key == pygame.K_s:
                spielfigur_1_bewegung = +6
            

            # Taste für Spieler 2
            elif event.key == pygame.K_UP:
                spielfigur_2_bewegung = -6
            elif event.key == pygame.K_DOWN:
                spielfigur_2_bewegung = +6
        
        #zum Stoppen der Spielerbewegung 
        if event.type == pygame.KEYUP:
            

            # Tasten für Spieler 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                spielfigur_1_bewegung = 0
            
            # Tasten für Spieler 2
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spielfigur_2_bewegung = 0



    # Spiellogik hier integrieren
    if spielfigur_1_bewegung != 0:
        spielfigur_1_y += spielfigur_1_bewegung

    if spielfigur_1_y < 0:
        spielfigur_1_y = 0

    if spielfigur_1_y > FENSTERHOEHE - schlaegerhoehe:
        spielfigur_1_y = FENSTERHOEHE - schlaegerhoehe

    if spielfigur_2_bewegung != 0:
        spielfigur_2_y += spielfigur_2_bewegung

    if spielfigur_2_y < 0:
        spielfigur_2_y = 0

    if spielfigur_2_y > FENSTERHOEHE - schlaegerhoehe:
        spielfigur_2_y = FENSTERHOEHE - schlaegerhoehe

    if spielfigur_2_x < (ball.xPosGeben() + 20) and spielfigur_2_y < ball.yPosGeben() and (spielfigur_2_y + 60) > ball.yPosGeben():
        ball.umdrehen()

    if (spielfigur_1_x + 20) > ball.xPosGeben() and spielfigur_1_y < ball.yPosGeben() and (spielfigur_1_y + 60) > ball.yPosGeben():
        ball.umdrehen()


    
    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
    hintergrundErstellen()
    #Ball
    ball.bewegen()
    # -- Spielerfigur 1
    spieler1 = pygame.draw.rect(screen, WEISS, [spielfigur_1_x, spielfigur_1_y, 20, schlaegerhoehe])
    # -- Spielerfigur 2
    spieler2 = pygame.draw.rect(screen, WEISS, [spielfigur_2_x, spielfigur_2_y, 20, schlaegerhoehe])
    if ball.xPosGeben() < 5:
        gewinnerAnzeigen("Spieler 2 hat gewonnen")
        punkteSp2 += 1

    elif ball.xPosGeben() > (FENSTERBREITE -25):
        gewinnerAnzeigen("Spieler 1 hat gewonnen")
        punkteSp1 += 1


    #  Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)


pygame.quit()