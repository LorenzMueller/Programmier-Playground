
import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('example2.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Beispiel-Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personen (
        id INTEGER PRIMARY KEY,
        vorname VARCHAR(20),
        nachname VARCHAR(20),
        stand INTEGER
    );"""
)


# Beispiel-Datensätze in die Tabelle einfügen
cursor.execute("INSERT INTO personen (vorname, nachname, stand) VALUES (?, ?, ?)", ('Max', 'Mustermann', "1.1.1999"))
cursor.execute("INSERT INTO personen (vorname, nachname, stand) VALUES (?, ?, ?)", ('Anna', 'Müller', "1.1.1999"))
cursor.execute("INSERT INTO personen (vorname, nachname, stand) VALUES (?, ?, ?)", ('Peter', 'Schmidt', "1.1.1999"))

# Änderungen in der Datenbank speichern
conn.commit()

cursor.execute("SELECT nachname FROM personen")
inhalt = cursor.fetchall()
print(inhalt)

# Verbindung zur Datenbank schließen
conn.close()