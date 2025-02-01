"""
Module for script
"""

import requests

def generate_message(contract_address, method, params):
    """
    Generates a message for the given contract address, method, and params.
    """
    message = {
        "address": contract_address,
        "method": method,
        "params": params
    }
    return message

def send_message(message, api_endpoint):
    """
    Sends a message to the specified API endpoint.
    """
    response = requests.post(api_endpoint, json=message)
    return response.json()

CONTRACT_ADDRESS = "0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e"
API_ENDPOINT_TESTNET = "https://testnet.ton.org/api"
API_ENDPOINT_FASTNET = "https://fastnet.ton.org/api"
METHOD = "validate_block"
PARAMS = {
    "block_data": "block data",
    "collated_data": "collated data"
}

# Testnet
MESSAGE_TESTNET = generate_message(CONTRACT_ADDRESS, METHOD, PARAMS)
RESPONSE_TESTNET = send_message(MESSAGE_TESTNET, API_ENDPOINT_TESTNET)
print("Testnet Response:", RESPONSE_TESTNET)

# Fastnet
MESSAGE_FASTNET = generate_message(CONTRACT_ADDRESS, METHOD, PARAMS)
RESPONSE_FASTNET = send_message(MESSAGE_FASTNET, API_ENDPOINT_FASTNET)
print("Fastnet Response:", RESPONSE_FASTNET)
