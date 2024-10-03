from cryptography.fernet import Fernet

# Generiert einen Schlüssel zur Verschlüsselung
def generiere_schluessel():
    schluessel = Fernet.generate_key()
    with open("secret.key", "wb") as schluessel_datei:
        schluessel_datei.write(schluessel)

# Lädt den zuvor generierten Schlüssel
def lade_schluessel():
    return open("secret.key", "rb").read()

# Verschlüsselt die Datei
def verschluessel_datei(dateipfad):
    schluessel = lade_schluessel()
    fernet = Fernet(schluessel)
    
    with open(dateipfad, "rb") as datei:
        original_inhalt = datei.read()

    # Verschlüsselt den Inhalt
    verschluesselter_inhalt = fernet.encrypt(original_inhalt)
    
    with open(dateipfad, "wb") as verschluesselte_datei:
        verschluesselte_datei.write(verschluesselter_inhalt)
    
    print(f"Datei '{dateipfad}' erfolgreich verschlüsselt.")

# Entschlüsselt die Datei
def entschluessel_datei(dateipfad):
    schluessel = lade_schluessel()
    fernet = Fernet(schluessel)

    with open(dateipfad, "rb") als verschluesselte_datei:
        verschluesselter_inhalt = verschluesselte_datei.read()

    # Entschlüsselt den Inhalt
    entschluesselter_inhalt = fernet.decrypt(verschluesselter_inhalt)

    with open(dateipfad, "wb") als entschluesselte_datei:
        entschluesselte_datei.write(entschluesselter_inhalt)

    print(f"Datei '{dateipfad}' erfolgreich entschlüsselt.")


# Beispielverwendung
generiere_schluessel()  # Schlüssel einmalig generieren und speichern
verschluessel_datei("bbc_telegram_bot.c.py")  # Datei verschlüsseln
# entschluessel_datei("bbc_telegram_bot.py")  # Datei entschlüsseln, wenn nötig
