from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

# Your wallet address
wallet = os.getenv('WALLET_ADDRESS')

# Networks to check
networks = {
    'Ethereum Sepolia': os.getenv('ETHEREUM_RPC_URL'),
    'Base Sepolia': os.getenv('BASE_RPC_URL'),
    'Polygon Amoy': os.getenv('POLYGON_RPC_URL'),
    'Arbitrum Sepolia': os.getenv('ARBITRUM_RPC_URL'),
    'BSC Testnet': os.getenv('BSC_RPC_URL')
}

print(f"💼 Checking balances for: {wallet}\n")
print("="*60)

for name, rpc in networks.items():
    try:
        # Connect to network
        w3 = Web3(Web3.HTTPProvider(rpc))

        # Get balance (in Wei)
        balance_wei = w3.eth.get_balance(wallet)

        # Convert to ETH
        balance_eth = w3.from_wei(balance_wei, 'ether')

        # Display
        print(f"✅ {name:20} {balance_eth:>10.4f} ETH")

    except Exception as e:
        print(f"❌ {name:20} Error: {str(e)[:30]}")

print("="*60)
