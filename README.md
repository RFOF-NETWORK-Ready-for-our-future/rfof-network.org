# BUBATZ-TOKEN-QUELL-CODE---S
.github/└── workflows/└── build-and-run-bot.yml/telegram_bot.c 
mkdir RFOF_BOT
cd RFOF_BOT
python3 -m venv venv
source venv/bin/activate
pip install pycurl
nano telegram_bot.c
git add . 
git commit -m "Add GitHub Actions workflow and telegram_bot.c" 
git push origin main
git add . 
git commit -m "Add GitHub Actions workflow and telegram_bot.c" 
git push origin main

 👋 Welcome to the TOKEN BOT.
"@RFOF_BOT API Token 6774549752:AAFx5D-reu3Pu- qkmKLh2aNxumv4faZtRN0"
(You can change your language:
"🇬🇧English . . . . . . /langen
🇷🇺Русский . . . . . . /langru

Collaborative translations:
🇵🇸Arabic     [ 83%] . /langar
🇧🇷Brazil     [ 64%] . /langbr
🇨🇳Chinese    [ 53%] . /langcn
🇪🇸Español    [ 77%] . /langes
🇫🇷Francais   [ 54%] . /langfr
🇮🇱Hebrew     [ 44%] . /langhe
🇮🇩Indonesian [ 62%] . /langid
🇮🇹Italian    [ 46%] . /langit
🇲🇾Melayu     [ 67%] . /langms
🇺🇿О'zbek     [ 54%] . /languz
🇮🇷Persian    [ 57%] . /langfa
🇹🇷Türkçe     [ 89%] . /langtr"

Needs to be translated:
Deutsch    [ 37%]
Українська [ 44%]

▍To participate this translation)
▍@SatoOwnerOfficial
💎MEME COIN (BBC)  🔗 TON   🏛️ 0,2Lp
100k $BBC AIRDROP✈️

"👨‍👩‍👧‍👦 2 holders: 100% | 0%
@Satoramy
@SatoOwnerOfficial"
"token Contract:⭐👑🚀 EQDYMCZF6OADTVHJMA887WHDYH_DOWJYWOIOF9ZY5MM5-Q8D"

💎 MCap: 0,7 $USDT |
                   0,2 $TON
💲 Price: $N/A 5m undefined% 1h undefined% 24h undefined% 1W
📊
Buys:  undefined
Sells:  undefined
Volume 24h:  undefined.
💧 TON in LP: 0,2 TON.
🕰️ Age: N/A.
🍰 Supply: 1.00e+7T.
❌ Ownership renounced:
no.

Balance: 0.200 TON/$1.52  

📈 chart    🔍 scanner
👆👆👆👆👆👆👆👆📊
Chart undd scanner comment on the first of August two thousand and twenty-four platform Ston.fi & DeDust.io = 2 | Look forward to new trends and trading opportunities with the $TOKEN (Staking, Mining, trading and swapping) 🚀📊🌏🏙️🪩👑✨
Mintable: ❌ Yes (Owner)echo "# - https://github.com/RFOF-NETWORK/BUBATZ-TOKEN-QUELL-CODE---S.git-" >> README.md
git init
git add README.md
git commit -m "erstes Commit"
git branch -M main
git remote origin https://github.com/RFOF-NETWORK/BUBATZ-TOKEN-QUELL-CODE---S.git
git push -u origin main

name: @RFOF_BOT

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest  

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup MSYS2
        uses: msys2/setup-msys2@v2
        with:
          msystem: UCRT64
          update: true
          install: git mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-curl

      - name: Compile Telegram Bot
        run: |
          gcc -o telegram_bot telegram_bot.c -lcurl  

      - name: Run Telegram Bot
        run: |
          ./telegram_bot
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#define TOKEN "AAFx5D-reu3Pu-qkmKLh2aNxumv4faZtRN0"
#define CHAT_ID "6774549752"

git add .
git commit -m "Add GitHub Actions workflow and telegram_bot.c"
git push origin main
curl -X POST "https://api.telegram.org/botAAFx5D-reu3Pu-qkmKLh2aNxumv4faZtRN0/sendMessage" -d "chat_id=6774549752&text=Hallo, dies ist ein Test!"

char *url_encode(const char *str) {
    CURL *curl = curl_easy_init();
    char *encoded = NULL;

    if (curl) {
        encoded = curl_easy_escape(curl, str, 0);
        curl_easy_cleanup(curl);
    }

    return encoded;
}

void send_message(const char *message) {
    CURL *curl;
    CURLcode res;

    char url[256];
    snprintf(url, sizeof(url), "https://api.telegram.org/bot%s/sendMessage", TOKEN);
    printf("URL: %s\n", url);

    char *encoded_message = url_encode(message);
    if (!encoded_message) {
        fprintf(stderr, "Failed to URL encode the message\n");
        return;
    }

    char post_fields[512];
    snprintf(post_fields, sizeof(post_fields), "chat_id=%s&text=%s", CHAT_ID, encoded_message);
    printf("Post Fields: %s\n", post_fields);

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post_fields);

        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            printf("Message sent successfully!\n");
        }

        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize curl\n");
    }

    curl_global_cleanup();
    curl_free(encoded_message); chmod +x run_telegram_bot.sh

}

void process_command(const char *command) {
    printf("Processing command: %s\n", command);
    if (strcmp(command, "/start") == 0) {
        send_message("Willkommen beim Token Help Bot! Hier sind die verfügbaren Befehle: /info, /price, /buy, /sell, /transactions, /security, /support, /news, /community, /empty");
    } else if (strcmp(command, "/info") == 0) {
        send_message("Hi, I'm BUBATZ. Welcome to the TOKEN BOT. I'd like to give you an explanation. The $BBC Token is an innovative meme token based on the TON Blockchain (Telegram Open Network). Our goal is to provide financial support and political advocacy for the cannabis culture in a straightforward manner. To ensure simplicity and direct use, we aim to avoid complex apps or websites.");
    } else if (strcmp(command, "/price") == 0) {
        send_message("Der aktuelle Preis des Tokens beträgt 0,000000");
    } else if (strcmp(command, "/buy") == 0) {
        send_message("Anleitungen zum Kauf von Tokens: At the date 01.01.2024 we launch our token with SHIBA INU on TON INU🧿📘");
    } else if (strcmp(command, "/sell") == 0) {
        send_message("Anleitungen zum Verkauf von Tokens: At the date 01.08. You can hold my BBC Token on major websites: Ston.fi, DeDust.io, and Gecko🚀🚀🚀🚀🚀🚀🚀🚀🚀");
    } else if (strcmp(command, "/transactions") == 0) {
        send_message("Informationen zu Transaktionen: https://tonviewer.com/EQDk-1Gqc4YIC22LTAAZLxomhkyp-V52B0yaeHgmk3t9LgV_/jetton/EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D");
    } else if (strcmp(command, "/security") == 0) {
        send_message("Sicherheitstipps und Hinweise: https://tonviewer.com/privacy");
    } else if (strcmp(command, "/support") == 0) {
        send_message("Kontaktiere den Support für weitere Hilfe: @Satoramy @SatoOwnerOfficial");
    } else if (strcmp(command, "/news") == 0) {
        send_message("Neuigkeiten und Updates zum Token: https://t.me/+cygnO0t_nYM3ZGJi");
    } else if (strcmp(command, "/community") == 0) {
        send_message("Treten Sie unserer Community bei und diskutieren Sie mit anderen: https://t.me/BUBATZtokenOFFICIAL");
    } else if (strcmp(command, "/empty") == 0) {
        send_message("Liste wurde geleert.");
    } else {
        send_message("Unbekannter Befehl.");
    }
}

int main() {
    process_command("/start");
    process_command("/info");
    process_command("/price");
    process_command("/buy");
    process_command("/sell");
    process_command("/transactions");
    process_command("/security");
    process_command("/support");
    process_command("/news");
    process_command("/community");
    process_command("/empty");
    process_command("/unknown");

    return 0;
}
gcc -o telegram_bot telegram_bot.c -lcurl
./telegram_bot


# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.

If you discover a vulnerability in this project, please follow these steps:

1. **Contact**: Send an email to [rfof236286@gmail.com ] with details of the vulnerability.
2. **Acknowledgement**: You will receive an acknowledgment of your report within 48 hours.
3. **Assessment**: Our team will assess the vulnerability and determine its impact.
4. **Update**: You will receive updates on the progress of the fix. We aim to provide a fix within 7 days of reporting.
5. **Resolution**: Once the vulnerability is resolved, you will be informed, and the update will be rolled out.

Thank you for helping us keep our project secure.
README
# TOKEN QUELL CODE
# BUBATZ TOKEN QUELL CODE
