# Blockchain Implementation

This repository contains a simple blockchain implementation in Python, demonstrating core concepts like proof-of-work, block validation, and tamper detection.

## Features
- Proof-of-work mining with adjustable difficulty.
- Block validation to ensure the integrity of the blockchain.
- Genesis block creation and linked blocks.
- Demonstration of blockchain tampering detection.

---

## Prerequisites
- Python 3.7 or higher.

### Required Libraries
The implementation only uses standard Python libraries, so no additional installations are required.

---

## Setup and Execution

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
```

### Step 2: Navigate to the Directory
Move into the directory containing the code:
```bash
cd <repository-directory>
```

### Step 3: Run the Script
Execute the blockchain script:
```bash
python blockchain.py
```

### Output
1. **Mining blocks:** The script will demonstrate mining of two blocks and print their details, including:
   - Index
   - Timestamp
   - Transactions
   - Previous hash
   - Current hash
   - Nonce

2. **Tampering Simulation:** The script modifies a block to simulate tampering and then validates the chain, displaying an error if the chain is compromised.

---

## Example Output
### Mining Blocks:
```
Mining Block 1...
Mining Block 2...

Blockchain:
Block 0:
Timestamp: 1692638657.12345
Transactions: Genesis Block
Previous Hash: 0
Hash: 0000abcd12345...
Nonce: 1234
--------------------------------------------------
...
```

### Tampering Simulation:
```
Tampering with the blockchain...

Validating Blockchain...
Block 1 has been tampered with!
Blockchain integrity compromised!
```

---

## Key Components

### Block Class
- **Attributes:**
  - `index`, `transactions`, `previous_hash`, `timestamp`, `nonce`, `hash`.
- **Methods:**
  - `calculate_hash()`: Calculates the hash of the block.
  - `mine_block(difficulty)`: Mines the block using proof-of-work.

### Blockchain Class
- **Attributes:**
  - `chain`, `difficulty`.
- **Methods:**
  - `create_genesis_block()`: Creates the first block in the chain.
  - `add_block(new_block)`: Mines and adds a new block.
  - `is_chain_valid()`: Validates the integrity of the chain.

---

## Customization
You can modify the script as follows:
1. **Change the difficulty level:** Update the `difficulty` parameter in the `Blockchain` class to adjust mining complexity.
2. **Add new blocks:** Use the `add_block()` method with custom transactions.

---

## Author
Developed by Michael Philips.

