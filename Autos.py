class Fahrzeug():
    def __init__(self, farbe, baujahr, kmstand, sitze, marke, kofferaumvolumen = 100):
        """ Eigenschaften farbe, baujahr, kmstand, Sitzplätze, Marke erfassen """
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke
        self.kofferaumvolumen = kofferaumvolumen

    def hupen(self):
        """ hier sollte noch eine MP3-Datei ausgegeben werden """
        print("Trööt")

class Lkw(Fahrzeug):
    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        """ Eigenschaften farbe, baujahr, kmstand, Sitzplätze, Marke erfassen """
        super().__init__(farbe, baujahr, kmstand, sitze, marke, 200)

    def parken(self):
        print("Das Auto wurde am Frimenhof abgestellt")

    def aufladen(self, gewicht = 20):
        self.kofferaumvolumen -= gewicht
        print("Verbleibendes Volumen: ", self.kofferaumvolumen)


class Pkw(Fahrzeug):
    """ Klasse für das Erstellen von Personenkraftwagen """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        """ Eigenschaften farbe, baujahr, kmstand, Sitzplätze, Marke erfassen """
        super().__init__(farbe, baujahr, kmstand, sitze, marke)

    

    def fahren(self, km):
        """ wie viele KM gefahren werden, was dem Tachostand aufaddiert wird """
        self.kmstand += km
        print("Ich fahre ", km, " Kilometer")
        print("Insgesamt bin ich ", self.kmstand ," gefahren")

    def parken(self):
        """ neben fahren schon das größere Problem in Städten """
        print("Ich habe eine Parkplatz gefunden")

    def kilometerstand(self):
        """ Ausgabe des KM-Standes vom Tacho """
        print("Ich habe ", str(self.kmstand) ," auf dem Tacho")

trabi = Pkw("rot", 1981, 143000, 4, "Trabi")
trabi.hupen()
trabi.kilometerstand()
trabi.fahren(5)

brumi = Lkw("blau", 1950, 150003, 2, "LKW")
brumi.hupen()
brumi.aufladen()
brumi.aufladen(30)
