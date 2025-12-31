from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# Get wallet to check
print("🔍 WALLET SPY TOOL")
print("="*60)
wallet_input = input("Enter wallet address to check: ").strip()

# Validate address
if not wallet_input.startswith('0x') or len(wallet_input) != 42:
    print("❌ Invalid address format!")
    exit()

networks = {
    'Ethereum Sepolia': os.getenv('ETHEREUM_RPC_URL'),
    'Base Sepolia': os.getenv('BASE_RPC_URL'),
    'Polygon Amoy': os.getenv('POLYGON_RPC_URL'),
    'Arbitrum Sepolia': os.getenv('ARBITRUM_RPC_URL'),
}

print(f"\n💼 Checking: {wallet_input}\n")
print("="*60)

for name, rpc in networks.items():
    try:
        w3 = Web3(Web3.HTTPProvider(rpc))
        balance_wei = w3.eth.get_balance(wallet_input)
        balance_eth = w3.from_wei(balance_wei, 'ether')

        # Get transaction count (how many txs this wallet sent)
        tx_count = w3.eth.get_transaction_count(wallet_input)

        print(f"✅ {name:20}")
        print(f"   Balance: {balance_eth:>10.4f} ETH")
        print(f"   Transactions: {tx_count}\n")

    except Exception as e:
        print(f"❌ {name:20} Error\n")

print("="*60)
