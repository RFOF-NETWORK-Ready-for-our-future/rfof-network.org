import os
import requests
import logging
from dotenv import load_dotenv
from tonclient import TonClient, Abi, Contract, Message
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the TON Client
client = TonClient(network="mainnet")

# Define constants
CONTRACT_ADDRESS = "EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D"
ABI_FILE = "jetton_token.abi.json"
BASE_URL = "https://tonapi.io/v2"
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
CHAT_ID = "6774549752"

# Define the ABI for the Jetton Token
abi = Abi.from_file(ABI_FILE)

# Define API keys from environment variables
api_keys = {
    "storage_mapper_declarations": os.getenv("STORAGE_MAPPER_DECLARATIONS_API_KEY"),
    "token_rates": os.getenv("TOKEN_RATES_API_KEY"),
}

# Function to URL encode the message
def url_encode(message):
    return requests.utils.quote(message)

# Function to send a message via Telegram
def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        logger.error(f"Failed to send message: {response.status_code} - {response.text}")
    else:
        logger.info("Message sent successfully!")

# Function to get the balance of an address
def get_balance(address):
    try:
        result = client.call_function(
            Contract(abi, CONTRACT_ADDRESS),
            "balanceOf",
            {"account": address}
        )
        return result["value"]
    except Exception as e:
        logger.error(f"Error getting balance: {e}")
        return "Error retrieving balance"

# Function to transfer tokens
def transfer_tokens(from_address, to_address, amount, private_key):
    try:
        message = Message(
            to=CONTRACT_ADDRESS,
            body=Contract(abi, CONTRACT_ADDRESS).encode_function("transfer", {"to": to_address, "amount": amount}),
            keys={"private_key": private_key}
        )
        result = client.send_message(message)
        return result
    except Exception as e:
        logger.error(f"Error transferring tokens: {e}")
        return "Error during token transfer"

# Function to get token rates using the API key
def get_token_rates():
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['token_rates']}"
        }
        response = requests.get(f"{BASE_URL}/rates", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error getting token rates: {e}")
        return "Error retrieving token rates"

# Function to get Jettons for a specific account
def get_jettons(account_id):
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['storage_mapper_declarations']}"
        }
        response = requests.get(f"{BASE_URL}/accounts/{account_id}/jettons", headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error getting jettons: {e}")
        return "Error retrieving jettons"

# Telegram bot commands
def start(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Willkommen beim Token Help Bot! Hier sind die verfügbaren Befehle: /info, /price, /buy, /sell, /transactions, /security, /support, /news, /community, /empty")

def info(update: Update, context: CallbackContext):
    send_message(update.message.chat_id, "Hi, I'm BUBATZ. Welcome to the TOKEN BOT. I'd like to give you an explanation...")

def price(update: Update, context: CallbackContext):
    rates = get_token_rates()
    send_message(update.message.chat_id, f"Current token rates: {rates}")

def balance(update: Update, context: CallbackContext):
    try:
        address = context.args[0]  # Expecting the wallet address to be passed as an argument
        balance = get_balance(address)
        send_message(update.message.chat_id, f"Balance for {address}: {balance}")
    except IndexError:
        send_message(update.message.chat_id, "Please provide a wallet address.")

def transfer(update: Update, context: CallbackContext):
    try:
        from_address = context.args[0]
        to_address = context.args[1]
        amount = int(context.args[2])
        private_key = context.args[3]  # Be cautious with handling private keys
        result = transfer_tokens(from_address, to_address, amount, private_key)
        send_message(update.message.chat_id, f"Transfer result: {result}")
    except (IndexError, ValueError) as e:
        send_message(update.message.chat_id, f"Error: {e}")

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
    # Initialize the Telegram bot
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register handlers
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

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
