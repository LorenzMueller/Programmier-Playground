class Ball():
    def __init__(self, xPos, yPos, xRichtung, yRichtung, xAlt, yAlt):
        self.xPos = xPos
        self.yPos = yPos
        self.xRichtung = xRichtung
        self.yRichtung = yRichtung
        self.xAlt = xAlt
        self.yAlt = yAlt
    
    def set_xPos(self, new):
        self.xPos = new
    def set_yPos(self, new):
        self.yPos = new
    def set_xRichtung(self, new):
        self.xRichtung = new
    def set_yRichtung(self, new):
        self.yRichtung = new
    def set_xAlt(self, new):
        self.xAlt = new
    def set_yAlt(self, new):
        self.yAlt = new
    
    def get_xPos(self):
        return self.xPos
    def get_yPos(self):
        return self.yPos
    def get_xRichtung(self):
        return self.xRichtung
    def get_yRichtung(self):
        return self.yRichtung
    def get_xAlt(self):
        return self.xAlt
    def get_yAlt(self):
        return self.yAlt