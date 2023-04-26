datei = open("text.txt", "r")
i = 0
for zeile in datei:
    print("In Zeile",i ,"steht:", zeile)
    i += 1

print(datei.read())
datei.close()