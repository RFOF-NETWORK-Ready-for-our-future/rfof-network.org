#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

#define TOKEN "AAFx5D-reu3Pu-qkmKLh2aNxumv4faZtRN0"
#define CHAT_ID "6774549752"

char* url_encode(const char* str) {
    CURL* curl = curl_easy_init();
    char* encoded = NULL;

    if (curl) {
        encoded = curl_easy_escape(curl, str, 0);
        curl_easy_cleanup(curl);
    }

    return encoded;
}

void send_message(const char* message) {
    CURL* curl;
    CURLcode res;

    char url[256];
    snprintf(url, sizeof(url), "https://api.telegram.org/bot%s/sendMessage", TOKEN);
    printf("URL: %s\n", url);

    char* encoded_message = url_encode(message);
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
    curl_free(encoded_message);
}

void process_command(const char* command) {
    printf("Processing command: %s\n", command);

    if (strcmp(command, "/start") == 0) {
        send_message("Willkommen beim Token Help Bot! Hier sind die verfügbaren Befehle: /info, /price, /buy, /sell, /transactions, /security, /support, /news, /community, /empty");
    } else if (strcmp(command, "/info") == 0) {
        send_message("Hi, I'm BUBATZ. Welcome to the TOKEN BOT. I'd like to give you an explanation...");
    } else if (strcmp(command, "/price") == 0) {
        send_message("Der aktuelle Preis des Tokens beträgt 0,000000");
    } else if (strcmp(command, "/buy") == 0) {
        send_message("Anleitungen zum Kauf von Tokens...");
    } else if (strcmp(command, "/sell") == 0) {
        send_message("Anleitungen zum Verkauf von Tokens...");
    } else if (strcmp(command, "/transactions") == 0) {
        send_message("Informationen zu Transaktionen: https://tonviewer.com/...");
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
