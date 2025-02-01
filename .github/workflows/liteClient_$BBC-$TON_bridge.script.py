import requests

def generate_new_key_block_message(query_id, block, signatures):
    message = {
        "query_id": query_id,
        "block": block,
        "signatures": signatures
    }
    return message

def generate_check_transaction_message(query_id, transaction, proof, current_block):
    message = {
        "query_id": query_id,
        "transaction": transaction,
        "proof": proof,
        "current_block": current_block
    }
    return message

def send_message(message, api_endpoint):
    response = requests.post(api_endpoint, json=message)
    return response.json()

# Beispiel für das Abrufen von Daten vom Lite-Server und Erstellen von Nachrichten
api_endpoint = "https://testnet.ton.org/api"
query_id = 1
block = "block data"
signatures = "signatures data"
transaction = "transaction data"
proof = "proof data"
current_block = "current block data"

# Erstellen und Senden von Nachrichten
new_key_block_message = generate_new_key_block_message(query_id, block, signatures)
response = send_message(new_key_block_message, api_endpoint)
print(response)

check_transaction_message = generate_check_transaction_message(query_id, transaction, proof, current_block)
response = send_message(check_transaction_message, api_endpoint)
print(response)
