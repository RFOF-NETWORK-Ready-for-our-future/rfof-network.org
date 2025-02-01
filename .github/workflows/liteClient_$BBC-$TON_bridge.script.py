"""
Module for liteClient_$BBC-$TON_bridge.script
"""

import requests

def generate_new_key_block_message(query_id, block, signatures):
    """
    Generates a new key block message.
    """
    message = {
        "query_id": query_id,
        "block": block,
        "signatures": signatures
    }
    return message

def generate_check_transaction_message(query_id, transaction, proof, current_block):
    """
    Generates a check transaction message.
    """
    message = {
        "query_id": query_id,
        "transaction": transaction,
        "proof": proof,
        "current_block": current_block
    }
    return message

def send_message(message, api_endpoint):
    """
    Sends a message to the specified API endpoint.
    """
    response = requests.post(api_endpoint, json=message)
    return response.json()

API_ENDPOINT_TESTNET = "https://testnet.ton.org/api"
API_ENDPOINT_FASTNET = "https://fastnet.ton.org/api"
QUERY_ID = 1
BLOCK = "block data"
SIGNATURES = "signatures data"
TRANSACTION = "transaction data"
PROOF = "proof data"
CURRENT_BLOCK = "current block data"

# Testnet
NEW_KEY_BLOCK_MESSAGE_TESTNET = generate_new_key_block_message(QUERY_ID, BLOCK, SIGNATURES)
RESPONSE_TESTNET = send_message(NEW_KEY_BLOCK_MESSAGE_TESTNET, API_ENDPOINT_TESTNET)
print("Testnet Response:", RESPONSE_TESTNET)

CHECK_TRANSACTION_MESSAGE_TESTNET = generate_check_transaction_message(
    QUERY_ID, TRANSACTION, PROOF, CURRENT_BLOCK
)
RESPONSE_TESTNET = send_message(CHECK_TRANSACTION_MESSAGE_TESTNET, API_ENDPOINT_TESTNET)
print("Testnet Response:", RESPONSE_TESTNET)

# Fastnet
NEW_KEY_BLOCK_MESSAGE_FASTNET = generate_new_key_block_message(QUERY_ID, BLOCK, SIGNATURES)
RESPONSE_FASTNET = send_message(NEW_KEY_BLOCK_MESSAGE_FASTNET, API_ENDPOINT_FASTNET)
print("Fastnet Response:", RESPONSE_FASTNET)

CHECK_TRANSACTION_MESSAGE_FASTNET = generate_check_transaction_message(
    QUERY_ID, TRANSACTION, PROOF, CURRENT_BLOCK
)
RESPONSE_FASTNET = send_message(CHECK_TRANSACTION_MESSAGE_FASTNET, API_ENDPOINT_FASTNET)
print("Fastnet Response:", RESPONSE_FASTNET)
