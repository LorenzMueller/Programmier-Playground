class Taschenrechner():
    def __init__(self):
        self.zahl1 = 1
        self.zahl2 = 2
        self.wahrheit = True
        self.inhalt = ""
        self.name = ""

    def methode0(self):
        return self.zahl1 + self.zahl2
    def methode1(self):
        self.zahl1 = 15
    def methode2(self):
        self.wahrheit = False
    def methode3(self):
        self.zahl1 += 5
    def methode4(self):
        self.zahl1 = self.zahl2 *2
    def methode5(self):
        self.inhalt = "goofy"
    def methode6(self):
        self.name = "Ciccone"
    def methode7(self):
        self.inhalt += "Süüü"
    def methode8(self):
        temp1 = self.zahl1
        self.zahl1 = self.zahl2
        self.zahl2 = temp1
    def methode9(self):
        if(self.wahrheit == True):
            self.wahrheit = False
        else:
            self.wahrheit = True

taschenrechner = Taschenrechner()


#Testen der erstellten Methoden
print(taschenrechner.methode0())
taschenrechner.methode1()
print(taschenrechner.zahl1)
taschenrechner.methode2()
print(taschenrechner.wahrheit)
taschenrechner.methode3()
print(taschenrechner.zahl1)
taschenrechner.methode4()
print(taschenrechner.zahl1)
taschenrechner.methode5()
print(taschenrechner.inhalt)
taschenrechner.methode6()
print(taschenrechner.name)
taschenrechner.methode7()
print(taschenrechner.inhalt)


taschenrechner2 = Taschenrechner()
taschenrechner2.methode8()
print(str(taschenrechner2.zahl1) + " " + str(taschenrechner2.zahl2))
taschenrechner2.methode9()
print(taschenrechner2.wahrheit)
