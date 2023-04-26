import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('example.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Beispiel-Tabelle erstellen
sql_anweisung = """
CREATE TABLE IF NOT EXISTS personen (
vorname VARCHAR(20), 
nachname VARCHAR(30)
);"""

cursor.execute(sql_anweisung)

# Beispiel-Datensätze in die Tabelle einfügen
cursor.execute("INSERT INTO personen (vorname, nachname) VALUES (?, ?)", ('Max', 'Mustermann'))
cursor.execute("INSERT INTO personen (vorname, nachname) VALUES (?, ?)", ('Anna', 'Müller'))
cursor.execute("INSERT INTO personen (vorname, nachname) VALUES (?, ?)", ('Peter', 'Schmidt'))

# Änderungen in der Datenbank speichern
conn.commit()

# Verbindung zur Datenbank schließen
conn.close()