from loguru import logger
from block import Block

class Chain:
    def __init__(self):
        self.chain = []
        self.transction_count = 0
        self.transcations_per_block = 10
        self.buffer = []
        self.generate_genesis_block()

    @property
    def last_block(self):
        return self.chain[-1]

    def generate_genesis_block(self):
        self.chain.append(Block('Genesis Block ',['Genesis Block ']))

    def write_transaction(self, trasaction):
        self.transction_count = self.transction_count + 1
        self.buffer.append(str(trasaction))
        if self.transction_count % self.transcations_per_block == 0: #generate new block 
            logger.info("Generating new Block")
            previous_block_hash = self.last_block.block_hash
            self.chain.append(Block(previous_hash=previous_block_hash,transactions=self.buffer))
            self.buffer = []

    def print_chain(self):
        for i in range(len(self.chain)):
            logger.info(f"Hash {i + 1}: {self.chain[i].block_hash}")
            logger.info(f"Data {i + 1}: {self.chain[i].block_data}")
        logger.info(f"Total trascations on chain: {self.transction_count}")