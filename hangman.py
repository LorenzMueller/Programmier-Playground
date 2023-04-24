import random
#Eingaben
woerter = 'hund katze maus haus raus'.split()
erraten = []
nutzereingabe = ""
fehlversuche = 8
 
#Initialisierung
rate_wort = random.choice(woerter)
print(rate_wort)
for buchstaben in rate_wort:
    erraten.append('_')

#Hauptspiel
while nutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=" ")
    print()
    nutzereingabe = input("Ihr Vorschlag: ")
    x = 0
    for buchstabe in rate_wort:
        if buchstabe.lower() == nutzereingabe.lower():
            print("Treffer")
            erraten[x] = buchstabe
            break
        x += 1
        if x >= len(rate_wort):
            fehlversuche -= 1
    
    if '_' in erraten:
        
        print("Du hast noch ", fehlversuche)
        if fehlversuche == 0:
            print("Schade")
    else:
        print("gewonnen, das Wort war", rate_wort)
        break