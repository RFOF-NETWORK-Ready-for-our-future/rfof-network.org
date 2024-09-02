import requests
from tonclient import TonClient, Abi, Contract, Message
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the TON Client
client = TonClient(network="mainnet")

# Define the ABI for the Jetton Token
abi = Abi.from_file("jetton_token.abi.json")

# Define the contract address
contract_address = "EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D"

# Define API keys from environment variables
api_keys = {
    "storage_mapper_declarations": os.getenv("STORAGE_MAPPER_DECLARATIONS_API_KEY"),
    "token_rates": os.getenv("TOKEN_RATES_API_KEY"),
}

# Base URL for TON API
base_url = "https://tonapi.io/v2"

# Function to get the balance of an address
def get_balance(address):
    try:
        result = client.call_function(
            Contract(abi, contract_address),
            "balanceOf",
            {"account": address}
        )
        return result["value"]
    except Exception as e:
        print(f"Error getting balance: {e}")
        return "Error retrieving balance"

# Function to transfer tokens
def transfer_tokens(from_address, to_address, amount, private_key):
    try:
        message = Message(
            to=contract_address,
            body=Contract(abi, contract_address).encode_function("transfer", {"to": to_address, "amount": amount}),
            keys={"private_key": private_key}
        )
        result = client.send_message(message)
        return result
    except Exception as e:
        print(f"Error transferring tokens: {e}")
        return "Error during token transfer"

# Function to get token rates using the API key
def get_token_rates():
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['token_rates']}"
        }
        response = requests.get(f"{base_url}/rates", headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error getting token rates: {e}")
        return "Error retrieving token rates"

# Function to get Jettons for a specific account
def get_jettons(account_id):
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['storage_mapper_declarations']}"
        }
        response = requests.get(f"{base_url}/accounts/{account_id}/jettons", headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error getting jettons: {e}")
        return "Error retrieving jettons"

# Function to verify a transaction
def verify_transaction(transaction_id):
    try:
        headers = {
            "Authorization": f"Bearer {api_keys['token_rates']}"
        }
        response = requests.get(f"{base_url}/transactions/{transaction_id}", headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error verifying transaction: {e}")
        return "Error verifying transaction"

# Function to create a new account
def create_account():
    # Note: Account creation in TON usually involves more steps and might require interacting with specific smart contracts.
    return "Account creation not implemented in this example."

# Telegram bot commands
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the BUBATZ Token Bot! Use /info to get information about the BUBATZ Token.")

def info(update: Update, context: CallbackContext):
    update.message.reply_text("BUBATZ Token: Information about the token and its goals.")

def price(update: Update, context: CallbackContext):
    rates = get_token_rates()
    update.message.reply_text(f"Current token rates: {rates}")

def balance(update: Update, context: CallbackContext):
    try:
        address = context.args[0]  # Expecting the wallet address to be passed as an argument
        balance = get_balance(address)
        update.message.reply_text(f"Balance for {address}: {balance}")
    except IndexError:
        update.message.reply_text("Please provide a wallet address.")

def transfer(update: Update, context: CallbackContext):
    try:
        from_address = context.args[0]
        to_address = context.args[1]
        amount = int(context.args[2])
        private_key = context.args[3]  # Be cautious with handling private keys
        result = transfer_tokens(from_address, to_address, amount, private_key)
        update.message.reply_text(f"Transfer result: {result}")
    except (IndexError, ValueError) as e:
        update.message.reply_text(f"Error: {e}")

def get_jettons(update: Update, context: CallbackContext):
    try:
        account_id = context.args[0]
        jettons = get_jettons(account_id)
        update.message.reply_text(f"Jettons for account {account_id}: {jettons}")
    except IndexError:
        update.message.reply_text("Please provide an account ID.")

def verify(update: Update, context: CallbackContext):
    try:
        transaction_id = context.args[0]
        verification = verify_transaction(transaction_id)
        update.message.reply_text(f"Transaction verification: {verification}")
    except IndexError:
        update.message.reply_text("Please provide a transaction ID.")

def create(update: Update, context: CallbackContext):
    update.message.reply_text(create_account())

def main():
    # Initialize the Telegram bot
    updater = Updater(os.getenv("TELEGRAM_BOT_API_KEY"), use_context=True)
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(CommandHandler("transfer", transfer))
    dp.add_handler(CommandHandler("get_jettons", get_jettons))
    dp.add_handler(CommandHandler("verify", verify))
    dp.add_handler(CommandHandler("create", create))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
