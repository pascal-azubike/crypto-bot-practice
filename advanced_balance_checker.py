from web3 import Web3
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

wallet = os.getenv('WALLET_ADDRESS')

networks = {
    'Ethereum Sepolia': os.getenv('ETHEREUM_RPC_URL'),
    'Base Sepolia': os.getenv('BASE_RPC_URL'),
    'Polygon Amoy': os.getenv('POLYGON_RPC_URL'),
    'Arbitrum Sepolia': os.getenv('ARBITRUM_RPC_URL'),
    'BSC Testnet': os.getenv('BSC_RPC_URL')
}

print(f"\n{'='*70}")
print(f"💼 WALLET BALANCE CHECKER")
print(f"{'='*70}")
print(f"📍 Address: {wallet}")
print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{'='*70}\n")

total_networks = len(networks)
connected_networks = 0
total_balance = 0

for name, rpc in networks.items():
    try:
        w3 = Web3(Web3.HTTPProvider(rpc))

        # Get balance
        balance_wei = w3.eth.get_balance(wallet)
        balance_eth = w3.from_wei(balance_wei, 'ether')

        # Get latest block
        block = w3.eth.block_number

        # Get gas price
        gas_price = w3.eth.gas_price
        gas_gwei = w3.from_wei(gas_price, 'gwei')

        connected_networks += 1
        total_balance += float(balance_eth)

        # Display with colors
        status = "💰" if balance_eth > 0 else "⚪"
        print(f"{status} {name:20}")
        print(f"   Balance: {balance_eth:>10.4f} ETH")
        print(f"   Block:   {block:>10,}")
        print(f"   Gas:     {gas_gwei:>10.2f} Gwei\n")

    except Exception as e:
        print(f"❌ {name:20} - Connection Failed\n")

print(f"{'='*70}")
print(f"📊 SUMMARY")
print(f"{'='*70}")
print(f"Networks Connected: {connected_networks}/{total_networks}")
print(f"Total Balance: {total_balance:.4f} ETH (testnet)")
print(f"{'='*70}\n")
