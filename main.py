from loguru import logger
from chain import Chain

logger.info("Initializing Blockchain")

chain = Chain()

for i in range(100):
    chain.write_transaction(i)

#chain.print_chain()