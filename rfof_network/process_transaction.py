import os
import requests
import logging
from dotenv import load_dotenv
from tonclient import TonClient, Abi, Contract, Message
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Umgebungsvariablen laden
load_dotenv()

# Konstanten und Konfigurationen
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
CHAT_ID = os.getenv("CHAT_ID", "6386147374")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D")
ABI_FILE = "jetton_token.abi.json"
BASE_URL = "https://tonapi.io/v2"
LIQUIDITY_POOL_ADDRESS = "EQDoEf5ZMYN-fEvfu-DPoBsxt_ErDo9bxujTc6_FeWH_VGU8"

# API-Keys
api_keys = {
    "storage_mapper_declarations": os.getenv("STORAGE_MAPPER_DECLARATIONS_API_KEY"),
    "token_rates": os.getenv("TOKEN_RATES_API_KEY"),
}

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TON Client initialisieren
client = TonClient(network="mainnet")

# ABI für das Jetton Token definieren
abi = Abi.from_file(ABI_FILE)

# Gebührenberechnung
def calculate_fee(amount):
    fee_percentage = 0.0001  # 0,01%
    fee = amount * fee_percentage
    return fee

# Tokens senden
def send_tokens(sender, recipient, amount):
    # Implementiere den Code zum Senden von Tokens
    # Dies ist ein Platzhalter für die eigentliche Implementierung
    logger.info(f"Sending {amount} tokens from {sender} to {recipient}")
    pass

# Transaktion verarbeiten
def process_transaction(sender, recipient, amount):
    try:
        # Berechnung der Gebühr
        fee = calculate_fee(amount)
        amount_after_fee = amount - fee
        
        # Durchführung der Haupttransaktion
        send_tokens(sender, recipient, amount_after_fee)
        
        # Gebühr an den Liquiditätspool senden
        send_tokens(sender, LIQUIDITY_POOL_ADDRESS, fee)
        
        return "Transaktion erfolgreich verarbeitet."
    except Exception as e:
        logger.error(f"Fehler bei der Verarbeitung der Transaktion: {e}")
        return "Fehler bei der Verarbeitung der Transaktion."

# Nachricht über Telegram senden
def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        logger.error(f"Nachricht konnte nicht gesendet werden: {response.status_code} - {response.text}")
    else:
        logger.info("Nachricht erfolgreich gesendet!")

# Guthaben einer Adresse abrufen
def get_balance(address):
    try:
        result = client.call_function(
            Contract(abi, CONTRACT_ADDRESS),
            function="getBalance",
            params={"address": address}
        )
        return result
    except Exception as e:
        logger.error(f"Fehler beim Abrufen des Guthabens: {e}")
        return "Fehler beim Abrufen des Guthabens"

# Token-Kurse abrufen
def get_token_rates():
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['token_rates']}"
        }
        response = requests.get(f"{BASE_URL}/rates", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Fehler beim Abrufen der Token-Kurse: {e}")
        return "Fehler beim Abrufen der Token-Kurse"

# Jettons für ein bestimmtes Konto abrufen
def get_jettons(account_id):
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['storage_mapper_declarations']}"
        }
        response = requests.get(f"{BASE_URL}/accounts/{account_id}/jettons", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Fehler beim Abrufen der Jettons: {e}")
        return "Fehler beim Abrufen der Jettons"

# Telegram-Bot-Befehle
def start(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Willkommen beim Token Help Bot! Hier sind die verfügbaren Befehle: /info, /price, /balance, /transfer, /transactions, /security, /support, /news, /community, /empty")

def info(update: Update, context: CallbackContext):
    message = (
        f"Token Info:\n"
        f"Total Supply: 999999999999999999999999900\n"
        f"Mintable: true\n"
        f"Admin Address: 0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e\n"
        f"Master Address: EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D\n"
        f"Jetton Content: Metadata about the token\n"
        f"Jetton Wallet Code: Smart contract code for the Jetton wallet"
    )
    send_message(update.message.chat_id, message)

def price(update: Update, context: CallbackContext):
    rates = get_token_rates()
    send_message(update.message.chat_id, f"Aktuelle Token-Kurse: {rates}")

def balance(update: Update, context: CallbackContext):
    try:
        address = context.args[0]
        balance = get_balance(address)
        send_message(update.message.chat_id, f"Guthaben für {address}: {balance}")
    except IndexError:
        send_message(update.message.chat_id, "Bitte geben Sie eine Wallet-Adresse an.")

def transfer(update: Update, context: CallbackContext):
    try:
        from_address = context.args[0]
        to_address = context.args[1]
        amount = int(context.args[2])
        result = process_transaction(from_address, to_address, amount)
        send_message(update.message.chat_id, f"Ergebnis der Übertragung: {result}")
    except (IndexError, ValueError) as e:
        send_message(update.message.chat_id, f"Fehler: {e}")

def transactions(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Informationen zu Transaktionen: https://tonviewer.com/...")

def security(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Sicherheitstipps und Hinweise: https://tonviewer.com/privacy")

def support(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Kontaktiere den Support für weitere Hilfe: @Satoramy @SatoOwnerOfficial")

def news(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Neuigkeiten und Updates zum Token: https://t.me/+cygnO0t_nYM3ZGJi")

def community(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Treten Sie unserer Community bei und diskutieren Sie mit anderen: https://t.me/BUBATZtokenOFFICIAL")

def empty(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Liste wurde geleert.")

def handle_unknown(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Unbekannter Befehl.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    logger.info("Bot ist gestartet")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("transfer", transfer))
    dp.add_handler(CommandHandler("transactions", transactions))
    dp.add_handler(CommandHandler("security", security))
    dp.add_handler(CommandHandler("support", support))
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(CommandHandler("community", community))
    dp.add_handler(CommandHandler("empty", empty))
    dp.add_handler(CommandHandler("unknown", handle_unknown))

    updater.start_polling()
    logger.info("Bot polling gestartet")
    updater.idle()

if __name__ == "__main__":
    main()
