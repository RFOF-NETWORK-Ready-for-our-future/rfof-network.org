import requests

def generate_message(contract_address, method, params):
    message = {
        "address": contract_address,
        "method": method,
        "params": params
    }
    return message

def send_message(message, api_endpoint):
    response = requests.post(api_endpoint, json=message)
    return response.json()

contract_address = "0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e"
api_endpoint = "https://testnet.ton.org/api"
method = "validate_block"
params = {
    "block_data": "block data",
    "collated_data": "collated data"
}

message = generate_message(contract_address, method, params)
response = send_message(message, api_endpoint)
print(response)
