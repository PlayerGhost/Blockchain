from Blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.addBlock("Atapo")
    blockchain.addBlock("Atapo")
    blockchain.addBlock("Atapo")

    blockchain.printAllBlockData()

    #blockchain.printBlocksHash()
