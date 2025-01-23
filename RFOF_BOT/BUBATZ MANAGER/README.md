BUBATZ Token Bot

Welcome to the BUBATZ Token Bot! This is a Telegram bot designed to provide information about the BUBATZ Token, including its price, buying and selling instructions, recent transactions, and more. The bot is implemented in Python and uses the `python-telegram-bot` library for interacting with the Telegram API.

# Token und Chat-ID aus Umgebungsvariablen lesen
TOKEN = os.getenv("TELEGRAM_BOT_API_KEY")
CHAT_ID = ("TELEGRAM_CHAT_ID")  # Hier die spezifische Chat-ID einfügen


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Security Policies](#security-policies)
- [License](#license)

## Installation

To set up the bot locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RFOF-NETWORK/BUBATZ-TOKEN-QUELL-CODE---S.git
    ```
   
2. **Navigate to the directory**:
    ```bash
    cd BUBATZ-TOKEN-QUELL-CODE---S
    ```

3. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install cryptography
    ```
**npm-install-@RFOF-BOT**

5. **Run the bot**:
    ```bash
    python path/to/your_script.py  # Replace with the actual path to your Python script
    ```

## Usage

The bot processes various Telegram commands to provide information about the BUBATZ Token. It executes predefined commands on startup but can be customized to handle specific user inputs.

Here’s an example of a function that provides information about the BUBATZ Token:

```python
def info(update: Update, context: CallbackContext):
    message = (
        f"Token Info:\n"
        f"Total Supplmf"Total Supply: 999999999999999999999999900\n"
        f"Mintable: true\n"
        f"Admin Address: 0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e\n"
        f"Master Address: EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D\n"
        f"Wallet Address: EQC_LhrYP8fvFgtDLEhrWnuSLo8w4cCI4o-CFSIGOCOTmwjj\n"
        f"Holder Address: EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D\n"
        f"Hey Hash: 8da55a166c83c8cea677f2fbb4925ef81eda782cee73bacaa82d5c4e87882138\n"
        f"Jetton Content: Contains metadata of the token, such as the name and description.\n"
        f"Jetton Wallet Code: The code of the smart contract that defines the logic for the Jetton wallet."
    )
    send_message(update.message.chat_id, message)
```

This function constructs a message containing various details about the token and sends it to the chat where the command was issued. Customize the placeholders like `TOTAL_SUPPLY`, `MINTABLE`, etc., with actual values.

## Available Commands

Here are the commands currently supported by the bot:

- `/start`: Greeting and overview of available commands.
- `/info`: Information about the BUBATZ Token and its goals.
- `/price`: Current token price.
- `/buy`: Instructions on how to buy tokens.
- `/sell`: Instructions on how to sell tokens.
- `/transactions`: Information on recent transactions.
- `/security`: Security tips and guidelines.
- `/support`: Contact information for support.
- `/news`: Latest news and updates about the token.
- `/community`: Information about the community and how to join.
- `/empty`: Clears the list of commands.
- `/unknown`: Notification for an unknown command.

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow located in `.github/workflows/build-and-run-bot.yml`. The workflow automates the following steps:

1. **Checkout the repository**: Clones the repository onto an Ubuntu machine.
2. **Set up Python**: Installs the specified Python version.
3. **Install dependencies**: Installs the required Python packages from `requirements.txt`.
4. **Run the bot**: Executes the Python script for the Telegram bot.
5. **npm-install-@RFOF-NETWORK**
