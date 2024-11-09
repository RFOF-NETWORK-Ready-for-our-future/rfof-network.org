#RFOF-NETWORK
BLOCKCHAIN rfof-network.org Matrix-VALLIDATOR-Workflow
    PR     |    ∞AI
          \_/
$PRAI = RFOF¤
|
|——— RFOF_Spider-net‰


BUBATZ-TOKEN-QUELL-CODE---S/
│
├── .github/
│   └── workflows/
│       └── build-and-run-bot.yml
├── telegram_bot.c
├── README.md
├── SECURITY.md
└── LICENSE


# BUBATZ Token Bot

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

## Security Policies

If you discover a security vulnerability in this project, please follow these steps:

1. **Contact**: Send an email to [rfof236286@gmail.com](mailto:rfof236286@gmail.com) with details about the vulnerability.
2. **Acknowledgment**: You will receive an acknowledgment of your report within 48 hours.
3. **Assessment**: Our team will assess the vulnerability and determine its impact.
4. **Update**: You will receive updates on the progress of the fix. We aim to provide a solution within 7 days.
5. **Resolution**: Once the vulnerability is resolved, you will be informed, and the update will be rolled out.

## License

This project is licensed under the [MIT License](LICENSE). For more details, see the LICENSE file.

# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

If you discover a vulnerability in this project, please follow these steps:

1. **Contact**: Send an email to [rfof236286@gmail.com](mailto:rfof236286@gmail.com) with details of the vulnerability.
2. **Acknowledgment**: You will receive an acknowledgment of your report within 48 hours.
3. **Assessment**: Our team will assess the vulnerability and determine its impact.
4. **Update**: You will receive updates on the progress of the fix. We aim to provide a fix within 7 days of reporting.
5. **Resolution**: Once the vulnerability is resolved, you will be informed, and the update will be rolled out.

Thank you for helping us keep our project secure.

# License Descriptions

## Open-Source Software Development

### GNU General Public License (GPL)

The GNU General Public License (GPL) is a free software license that ensures the end users have the freedom to run, study, share, and modify the software. The GPL requires that any modified versions of the software be distributed under the same license, preserving the same freedoms for future users.

**Key Points:**
- Freedom to use, study, and modify the software.
- Copyleft: Modified versions must also be open-source and licensed under GPL.
- No proprietary use.

For more details, see the full GPL text at [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.html).

### MIT License

The MIT License is a permissive free software license that allows developers to freely use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. It is often used for open-source projects where flexibility and simplicity are desired.

**Key Points:**
- Freedom to use, modify, and distribute.
- No warranty provided.
- Allows incorporation into proprietary software.

For more details, see the full MIT License text at [MIT License](https://opensource.org/licenses/MIT).

### Apache License 2.0

The Apache License 2.0 is a permissive license with an added grant of patent rights from the contributors to the users. It allows users to freely use, modify, and distribute the software, provided that the license terms are met.

**Key Points:**
- Allows for use, modification, and distribution.
- Provides an explicit grant of patent rights.
- Requires attribution and preservation of notices.

For more details, see the full Apache License 2.0 text at [Apache License](https://www.apache.org/licenses/LICENSE-2.0).

### Creative Commons Attribution 4.0 (CC BY 4.0)

The Creative Commons Attribution 4.0 License allows others to share, remix, adapt, and build upon the work, even commercially, as long as they credit the original creator. It is a flexible license designed for various types of works.

**Key Points:**
- Allows for sharing, adaptation, and commercial use.
- Requires attribution to the original creator.
- Does not impose additional restrictions.

For more details, see the full CC BY 4.0 text at [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Creative Commons Attribution-NonCommercial (CC BY-NC)

The Creative Commons Attribution-NonCommercial License allows others to use, remix, and build upon the work non-commercially, with credit given to the original creator. It is intended for creative works that are not intended for commercial use.

**Key Points:**
- Allows for non-commercial use and modification.
- Requires attribution to the original creator.
- Prohibits commercial use.

For more details, see the full CC BY-NC text at [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).

### Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)

The Creative Commons Attribution-NonCommercial-NoDerivatives License allows others to download and share the work, but not to modify it or use it commercially. It requires attribution to the original creator.

**Key Points:**
- Allows sharing without modification.
- Prohibits commercial use.
- Requires attribution to the original creator.

For more details, see the full CC BY-NC-ND text at [CC BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/).

### Creative Commons Attribution-ShareAlike (CC BY-SA)

The Creative Commons Attribution-ShareAlike License allows others to remix, tweak, and build upon the work, even commercially, as long as they credit the original creator and license their new creations under the identical terms.

**Key Points:**
- Allows for modification and commercial use.
- Requires attribution and similar licensing for derivative works.
- Promotes sharing

 under the same terms.

For more details, see the full CC BY-SA text at [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).

### Proprietary License

The Proprietary License grants specific rights to the licensee while retaining ownership of the intellectual property by the licensor. It typically includes restrictions on redistribution, modification, and usage.

**Key Points:**
- Grants exclusive rights to use and sometimes modify.
- Contains restrictions on redistribution and further licensing.
- Custom terms can be defined by the licensor.

For more details, see the specific terms provided by the licensor.

### GNU Affero General Public License (AGPL)

The GNU Affero General Public License (AGPL) is a free software license designed for software that is used over a network. It requires that any modified versions of the software be made available to the public, even when used as a service.

**Key Points:**
- Requires disclosure of source code modifications.
- Applies to software used over a network.
- Copyleft: Modified versions must also be licensed under AGPL.

For more details, see the full AGPL text at [GNU AGPL](https://www.gnu.org/licenses/agpl-3.0.html).

### Open Data Commons Open Database License (ODbL)

The Open Database License (ODbL) allows users to freely use, modify, and distribute databases while ensuring that any derived databases are also shared under the same license.

**Key Points:**
- Allows for use, modification, and distribution of databases.
- Requires attribution and preservation of license.
- Derived databases must also be shared under ODbL.

For more details, see the full ODbL text at [ODbL](https://opendatacommons.org/licenses/odbl/).

### Proprietary License with Research-Use Exception

This Proprietary License allows researchers to use proprietary technologies for non-commercial research purposes while retaining commercial rights with restrictions on redistribution and modification.

**Key Points:**
- Grants rights for non-commercial research use.
- Restricts commercial use and redistribution.
- Custom terms are defined by the licensor.

For more details, see the specific terms provided by the licensor.

### Proprietary Music License

The Proprietary Music License grants specific rights for the use of music for commercial purposes while protecting the rights of the original artist. It often includes terms related to usage, distribution, and modification.

**Key Points:**
- Allows commercial use of music.
- Protects the original artist's rights.
- Custom terms defined by the licensor.

For more details, see the specific terms provided by the licensor.

### GNU General Public License (GPL) for Plugins/Themes

Plugins and themes licensed under the GNU General Public License (GPL) ensure that modifications and distributions of these components remain open-source and are licensed under the same terms as the GPL.

**Key Points:**
- Ensures open-source licensing for plugins and themes.
- Requires sharing of modifications under GPL.
- Compatible with various e-commerce platforms.

For more details, see the full GPL text at [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.html).

### Proprietary License for Commercial Use

This Proprietary License allows for the use of digital products with specific restrictions and rights defined by the licensor. It typically includes terms related to usage, redistribution, and modification.

**Key Points:**
- Grants specific rights for commercial use.
- Includes restrictions on redistribution and modification.
- Custom terms defined by the licensor.

For more details, see the specific terms provided by the licensor.
```

Ich habe den `info`-Code-Snippet im Abschnitt `Usage` hinzugefügt, um den Lesern zu zeigen, wie sie die Bot-Funktion verwenden können.
