class BauplanKatzenKlasse():
    
    def __init__(self, rufname, farbe="schwarz", alter=0,schlafdauer = 0):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter
        self.schlafDauer = schlafdauer
    
    def miauen(self, anzahl = 1):
        for x in range(anzahl):
            print("Miau")
    
    def schlafen(self, minuten=5):
       self.schlafDauer += minuten
       print(self.rufname, " schläft jetzt ", self.schlafDauer , " Minuten ")

class Pkw():
    """ Klasse für das Erstellen von Personenkraftwagen """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke, geparkt = False):
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke
        self.geparkt = geparkt

    def hupen(self, anzahl = 2):
        for x in range(2):
            print("MEEP")
    
    def fahren(self, km):
        self.kmstand += km
        print("Aktueller KM Stand: ", self.kmstand)
    
    def parken(self):
        if self.geparkt == True:
            self.geparkt = False
        else:
            self.geparkt = True
        

trabi = Pkw("rot", 1981, 143000, 4, "Trabi")

trabi.parken()
print(trabi.geparkt)

"""katze_sammy = BauplanKatzenKlasse("Sammy", "orange", 8)
katze_klausi = BauplanKatzenKlasse("Klaus")
print(katze_sammy.farbe)
print(katze_klausi.farbe)
katze_klausi.miauen(5)
katze_klausi.schlafen(10)
katze_klausi.schlafen(10)"""

class Auto():

    def __init__(self, marke, farbe, ps):
        self.marke = marke
        self.farbe = farbe
        self.ps = ps

BMW = Auto("BMW", "rot", 321)

print(BMW.farbe)