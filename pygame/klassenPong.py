class Spieler():
    def __init__(self, xPos, yPos, bewegung, punkte, Schlaegerhoehe = 60):
        self.xPos = xPos
        self.yPos = yPos
        self.bewegung = bewegung
        self.punkte = punkte
        self.Schlaegerhoehe = 60

    def xPosGeben(self):
        return self.xPos
    def yPosGeben(self):
        return self.yPos
    def bewegungGeben(self):
        return self.bewegung
    
    def bewegungSetzen(self, bewegungNeu):
        self.bewegung = bewegungNeu
    def yPosVerschieben(self, yNeu):
        self.yPos += yNeu
    def yPosSetzen(self, yNeu):
        self.yPos = yNeu
    def punkteErhöhen(self):
        self.punkte += 1
    def punkteGeben(self):
        return self.punkte