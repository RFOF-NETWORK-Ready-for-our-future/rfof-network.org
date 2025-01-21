import time
import hashlib

class RFOFBlockchain:
    def __init__(self):
        self.blocks = []
        self.validators = []
        self.nano_data = {}
        self.storage_mapper = {}
        self.coin_master_address = "RFOF_CoinMaster_Address"
        self.founder_address = self.generate_wallet_address("Founder")
        self.vault = {}  # Tresor für gestakete Gebühren
        self.vault_timer = 30 * 24 * 60 * 60  # 30 Tage in Sekunden
        self.genesis_created = False
        self.liteserver_info = {
            "server_1": "31.57.199.1:5053",
            "public_key_1": "J4q7zg7JSVf5tXmAMQFsIeoTpQ6NaDIpcfgc0LUlg/c=",
            "server_2": "163.5.62.1:5053",
            "public_key_2": "J4q7zg7JSVf5tXmAMQFsIeoTpQ6NaDIpcfgc0LUlg/c="
        }
        self.bbc_info = {
            "address": "0:d831c65fe8e01db6f84999af3cef01ddc87fdda308d85a888e7fdcf2e4c9b9fa",
            "name": "BUBATZ COIN official (CSC/DCV).",
            "symbol": "BBC",
            "decimals": "9",
            "image": "https://cache.tonapi.io/imgproxy/cWW0mHZnCp-pZJWqMEdxQxKPW000jCEj793wY9-Kzcg/rs:fill:200:200:1/g:no/aHR0cHM6Ly9zdG9yYWdlLnlhbmRleGNsb3VkLm5ldC9taW50ZXItbG9nb3MvcXI5NTY4ZGoxdi5qcGc.webp",
            "description": "BBC Bubatz Meme Coin (BBC) – Die dezentrale Währung für Cannabis-Liebhaber. 🌿\n\nDer BBC Coin vereint Humor und Dezentralisierung"
        }
        self.owner_info = {
            "telegram_username": "@Satoramy",
            "ton_domain": "satoramy-on.ton",
            "public_key": "UQDk-1Gqc4YIC22LTAAZLxomhkyp-V52B0yaeHgmk3t9Lli6",
            "address": "0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e",
            "explorer_link": "EQDk-1Gqc4YIC22LTAAZLxomhkyp-V52B0yaeHgmk3t9LgV_"
        }

    def generate_wallet_address(self, label):
        # Erzeugt eine eindeutige Wallet-Adresse basierend auf dem Label
        return hashlib.sha256(f"{label}_{time.time()}".encode()).hexdigest()

    # #GENESIS_BLOCK
    def create_arc_genesis_reactor_block(self):
        if not self.genesis_created:
            # Zuerst wird der Genesis Block erstellt
            self.create_genesis_block()
            # Dann wird der ARC Genesis Reaktor Block erstellt und die Fusion initiiert
            arc_reactor_block = {
                "index": 1,
                "timestamp": time.time(),
                "data": "ARC Genesis Reaktor Block",
                "previous_hash": self.blocks[-1]["hash"],
                "hash": self.hash_block("ARC Genesis Reaktor Block"),
                "extra_features": self.initialize_arc_features()  # Eigene Funktionen des RFOF-Netzwerks
            }
            self.blocks.append(arc_reactor_block)
            self.genesis_created = True
            print("ARC Genesis Reaktor Block created with extra features.")
            self.fusion_genesis_arc()

    # #GENESIS_BLOCK
    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": self.hash_block("Genesis Block"),
            "extra_features": self.initialize_genesis_features()  # Funktionen des Bitcoin-Netzwerks
        }
        self.blocks.append(genesis_block)
        print("Genesis Block created.")

    # #FEATURES
    def initialize_genesis_features(self):
        features = {
            "Bitcoin_network": True,
            "transaction_processing": True
        }
        return features

    # #FEATURES
    def initialize_arc_features(self):
        features = {
            "PRAI_guardian": True,
            "nano_processing": True,
            "ColdNet_WarmNet": True,
            "Trash_to_Cash": True,
            "validator_creation": True
        }
        return features

    # #FUSION
    def fusion_genesis_arc(self):
        fusion_block = {
            "index": 2,
            "timestamp": time.time(),
            "data": "ARC Genesis Reactor Fusion Block",
            "previous_hash": self.blocks[-1]["hash"],
            "hash": self.hash_block("ARC Genesis Reactor Fusion Block"),
            "combined_features": {
                "Bitcoin_network": True,
                "PRAI_guardian": True,
                "nano_processing": True,
                "ColdNet_WarmNet": True,
                "Trash_to_Cash": True,
                "validator_creation": True
            }
        }
        self.blocks.append(fusion_block)
        print("ARC Genesis Reactor Fusion Block created.")
    # #HASH
    def hash_block(self, data):
        return str(hash(data))

    # #BLOCK_CREATION
    def create_block(self, transaction, from_address):
        previous_block = self.blocks[-1]
        block = self.generate_nanoblock(transaction, previous_block["hash"])
        self.blocks.append(block)
        self.handle_transaction_fee(transaction, from_address)
        return block

    # #BLOCK_CREATION
    def generate_nanoblock(self, transaction, previous_hash):
        nano_block = {
            "index": len(self.blocks),
            "timestamp": time.time(),
            "transaction": transaction,
            "data": self.process_data(transaction),
            "previous_hash": previous_hash,
            "hash": self.hash_block(transaction),
            "virtual_blocks": self.generate_virtual_blocks()
        }
        return nano_block

    # #DATA_PROCESSING
    def process_data(self, transaction):
        nano_data = {"compressed_data": str(transaction)[:10]}
        return nano_data

    # #VIRTUAL_BLOCKS
    def generate_virtual_blocks(self):
        virtual_blocks = []
        for i in range(1, 100000000001):
            virtual_block = {"block_id": i, "data": f"virtual_block_{i}"}
            virtual_blocks.append(virtual_block)
            if i % 100 == 0:
                self.create_validator(virtual_block)
        return virtual_blocks

    # #VALIDATORS
    def create_validator(self, virtual_block):
        validator = {"validator_id": len(self.validators) + 1, "virtual_block": virtual_block}
        self.validators.append(validator)
        self.create_block(f"Validator Transaction from Block {virtual_block['block_id']}", self.coin_master_address)
        print(f"Validator {validator['validator_id']} created from virtual block {virtual_block['block_id']}")

    # #TRANSACTION_FEES
    def handle_transaction_fee(self, transaction, from_address):
        fee = self.calculate_fee(transaction)
        self.store_fee_in_vault(fee, from_address)
        print(f"Transaction fee of {fee} units stored in vault from {from_address}")

    # #TRANSACTION_FEES
    def calculate_fee(self, transaction):
        return 0.01 * len(transaction)

    # #VAULT
    def store_fee_in_vault(self, fee, from_address):
        timestamp = time.time()
        self.vault[timestamp] = {"fee": fee, "from_address": from_address}

    # #VAULT
    def process_vault(self):
        current_time = time.time()
        for timestamp, fee_info in list(self.vault.items()):
            if current_time - timestamp >= self.vault_timer:
                fee = fee_info["fee"]
                from_address = fee_info["from_address"]
                self.release_fee_from_vault(fee, from_address)
                del self.vault[timestamp]

    # #VAULT
    def release_fee_from_vault(self, fee, from_address):
        if from_address == "External":
            self.storage_mapper[self.coin_master_address] = self.storage_mapper.get(self.coin_master_address, 0) + fee
        else:
            self.storage_mapper[from_address] = self.storage_mapper.get(from_address, 0) + fee
        print(f"Transaction fee of {fee} units released from vault to {from_address}")

class PRAI:
    def __init__(self):
        self.commands = []

    # #COMMANDS
    def receive_command(self, command):
        self.commands.append(command)
        return self.execute_command(command)

    # #COMMANDS
    def execute_command(self, command):
        if command == "create_block":
            blockchain = RFOFBlockchain()
            transaction = "Sample Transaction Data"
            from_address
