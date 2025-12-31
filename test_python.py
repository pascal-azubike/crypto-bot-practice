# Test your Python knowledge
from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get RPC URL
rpc_url = os.getenv('ETHEREUM_RPC_URL')

# Connect to Ethereum
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if connected
if w3.is_connected():
    print("✅ Connected to Ethereum!")
    print(f"Latest block: {w3.eth.block_number}")
else:
    print("❌ Connection failed")
