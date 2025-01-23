import hashlib
import time


class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # For proof-of-work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Generates the hash of the block by combining its contents.
        """
        block_content = (str(self.index) +
                         str(self.timestamp) +
                         str(self.transactions) +
                         str(self.previous_hash) +
                         str(self.nonce))
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Implements proof-of-work: the block's hash must start with a specific number of leading zeros.
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        """
        Creates the initial (genesis) block in the blockchain.
        """
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retrieves the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the chain after mining it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain's integrity.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has been tampered with!")
                return False

            # Check if the current block links to the previous block correctly
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i} is not linked to Block {i - 1}!")
                return False

        return True

    def print_chain(self):
        """
        Prints the details of all blocks in the chain.
        """
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)


# Run
if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain(difficulty=4)

    # Add blocks
    print("Mining Block 1...")
    blockchain.add_block(Block(1, ["Transaction 1", "Transaction 2"], blockchain.get_latest_block().hash))

    print("Mining Block 2...")
    blockchain.add_block(Block(2, ["Transaction 3", "Transaction 4"], blockchain.get_latest_block().hash))

    # Print the blockchain
    print("\nBlockchain:")
    blockchain.print_chain()

    # Tamper with the blockchain
    print("\nTampering with the blockchain...")
    blockchain.chain[1].transactions = ["Fake Transaction"]
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

    # Validate the blockchain
    print("\nValidating Blockchain...")
    if blockchain.is_chain_valid():
        print("Blockchain is valid!")
    else:
        print("Blockchain integrity compromised!")
