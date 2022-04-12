import hashlib

class Block:
    def __init__(self,previous_hash, transactions):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.block_data = ''.join(transactions) + previous_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()