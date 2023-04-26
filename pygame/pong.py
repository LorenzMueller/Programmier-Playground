import pygame

#Attribute
FENSTERBREITE = 640
FENSTERHOEHE = 480

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

# initialisieren von pygame
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
clock = pygame.time.Clock()
ball = Ball(10, 30, 20)

# Fenster öffnen
screen.fill(WEISS)

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

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
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")
                ball.bewegen()

        # Taste für Spieler 1
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")

            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
    # Spiellogik hier integrieren
    pygame.draw.ellipse(screen, WEISS, [10, 30, 20, 20])
    
    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
    screen.fill(SCHWARZ)
    ball.bewegen()
    #pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, 20, 20])
    
    #  Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)


pygame.quit()