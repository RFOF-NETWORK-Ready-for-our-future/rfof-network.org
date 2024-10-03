import os
import requests

# Token und Chat-ID aus Umgebungsvariablen lesen
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def url_encode(message):
    """URL-codiert eine Nachricht."""
    return requests.utils.quote(message)

def send_message(message):
    """Sendet eine Nachricht an den Telegram-Chat."""
    encoded_message = url_encode(message)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': encoded_message
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Nachricht erfolgreich gesendet!")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.text}")

def process_command(command):
    """Verarbeitet Befehle des Benutzers."""
    if command == "/start":
        send_message("Willkommen beim RFOF Bot! Hier sind die verfügbaren Befehle: /info, /price, /buy, /sell, /transactions, /security, /support, /news, /community, /empty")
    elif command == "/info":
        send_message("Hi, ich bin der RFOF Bot. Willkommen beim RFOF TOKEN BOT. Der $RFOF Token ist ein innovativer Token basierend auf der TON Blockchain.")
    elif command == "/price":
        send_message("Der aktuelle Preis des RFOF Tokens beträgt 0,000000.")
    elif command == "/buy":
        send_message("Anleitungen zum Kauf von RFOF Tokens folgen bald.")
    elif command == "/sell":
        send_message("Anleitungen zum Verkauf von RFOF Tokens folgen bald.")
    elif command == "/transactions":
        send_message("Informationen zu Transaktionen werden bald bereitgestellt.")
    elif command == "/security":
        send_message("Sicherheitstipps und Hinweise werden bald bereitgestellt.")
    elif command == "/support":
        send_message("Kontaktiere den Support für weitere Hilfe: @SupportHandle")
    elif command == "/news":
        send_message("Neuigkeiten und Updates zum RFOF Token werden bald bereitgestellt.")
    elif command == "/community":
        send_message("Treten Sie unserer Community bei und diskutieren Sie mit anderen: https://t.me/RFOFCommunity")
    elif command == "/empty":
        send_message("Liste wurde geleert.")
    else:
        send_message("Unbekannter Befehl.")

if __name__ == "__main__":
    commands = ["/start", "/info", "/price", "/buy", "/sell", "/transactions", "/security", "/support", "/news", "/community", "/empty", "/unknown"]
    for cmd in commands:
        process_command(cmd)
