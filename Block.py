from hashlib import sha256


class Block:

    def __init__(self, index, transactions, timestamp, previous_hash, nonce):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generateBlockHash()

    def generateBlockHash(self):
        blockData = str(self.index) + str(self.transactions) + \
                    str(self.timestamp) + str(self.previous_hash) + \
                    str(self.nonce)

        blockHash = sha256(blockData.encode()).hexdigest()

        return blockHash

    def printBlockData(self):
        print(f"Index: {self.index}")
        print(f"Hash: {self.hash}")
        print(f"Transações: {self.transactions}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Hash do bloco anterior: {self.previous_hash}")
        print(f"Nonce: {self.nonce}")
        print("--------------------------------------------------------------------")




