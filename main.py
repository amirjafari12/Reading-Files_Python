'''Man kann in python durch den Befehl open() Daten öffnen und die Dateien bearbeiten.
Dafür muss die Datei in demselben Pfad bringen, in welchen der Python Code läuft,
d.h. im selben Ordner. Mit dem Befehl read kann man auch die Datei lesen und wenn man
die Datei in eine for-schleife packt, kann man den Prozess des Lesens in Zeilen minimieren.'''

try:
    Datei_name = input("Bitte gebe hier dein Dateinamen ein: ")
    Datei_handle = open(Datei_name)

except:
    print("Diese Datei gibt es nicht")
    exit()

choose = input("Möchtest du nur die Zeilenanzahl deiner Datei mit einer Bedingung wissen? [y]\nMöchtest du die Anzahl deiner Datei mit den Schriften sehen? [j]\nWähle aus: ")

def nur_zeilen():
    count = 0
    for i in Datei_handle:
        if i.startswith("Subject: "):
            count = count + 1

    print(f"Es git {count} Zeilen in ihrer Datei mit dem treffenden Bedingung")


def zeilen_mit_schrift():
    count = 0
    for i in Datei_handle:
        if i.startswith("Subject: "):
            count = count + 1
            print(f"Zeile {count}")
            print(i)

    print(f"Es git {count} Zeilen in ihrer Datei mit dem treffenden Bedingung")

if choose == "y":
    nur_zeilen()

elif choose == "j":
    zeilen_mit_schrift()

else:
    print("Deine Angabe ist ungültig")
