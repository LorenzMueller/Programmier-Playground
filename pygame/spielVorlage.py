# Importieren der Pygame-Bibliothek
import pygame

# initialisieren von pygame
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS  = ( 255, 255, 255)

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
            if event.key == pygame.K_q:
                spielaktiv = False

        # Taste für Spieler 1
            elif event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
                pygame.draw.rect(screen, ROT, [10, 20, 100, 100], 1)
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
    
    # Spiellogik hier integrieren

    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)
    screen.fill(WEISS)
    pygame.draw.rect(screen, ROT, [10, 20, 100, 100], 1)
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)


pygame.quit()