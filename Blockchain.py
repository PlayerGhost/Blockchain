from Block import Block
from datetime import datetime
import time

class Blockchain:
    def __init__(self):
        self.blocks = []
        self.generateGenesisBlock()

    def generateGenesisBlock(self):
        genesisBlock = Block(0, "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
                             datetime.timestamp(datetime.now()), "0", 000)

        self.mine(genesisBlock)

        self.blocks.append(genesisBlock)

    def addBlock(self, transactions):
        newBlock = Block(len(self.blocks), transactions, datetime.timestamp(datetime.now()), self.blocks[-1].hash, 000)

        self.mine(newBlock)

        self.blocks.append(newBlock)

    def mine(self, block):
        startMiningTime = time.time()

        while not block.hash.startswith("000000"):
            block.nonce += 1
            block.hash = block.generateBlockHash()

        endMiningTime = time.time() - startMiningTime
        endMiningFormatted = datetime.fromtimestamp(endMiningTime).strftime('%M:%S.%f"')

        print(f"Bloco {block.index} minerado. Tempo decorrido: {endMiningFormatted}. Hash: {block.hash}")

    def printBlocksHash(self):
        for i in self.blocks:
            print(i.hash)

