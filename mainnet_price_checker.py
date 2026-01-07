"""
MAINNET PRICE CHECKER (Read-Only)
==================================
Check real token prices using your Alchemy account
"""

from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

# Use your Alchemy account but for MAINNET (read-only, no cost)
# Just change sepolia to mainnet in your key
alchemy_key = os.getenv('ETHEREUM_RPC_URL').split('/')[-1]
MAINNET_RPC = f'https://eth-mainnet.g.alchemy.com/v2/{alchemy_key}'

w3 = Web3(Web3.HTTPProvider(MAINNET_RPC))

print("🔌 Connecting to Ethereum mainnet...")

if not w3.is_connected():
    print("❌ Can't connect")
    exit()

print("✅ Connected!")
print(f"📦 Block: {w3.eth.block_number:,}\n")

print("💱 CHECKING REAL ETH PRICES")
print("="*60)


# Uniswap V2 Router
UNISWAP_ROUTER = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'

ROUTER_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            {"internalType": "address[]", "name": "path", "type": "address[]"}
        ],
        "name": "getAmountsOut",
        "outputs": [
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Token addresses
WETH = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
USDC = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'

router = w3.eth.contract(address=UNISWAP_ROUTER, abi=ROUTER_ABI)
amount_in = w3.to_wei(1, 'ether')

try:
    amounts = router.functions.getAmountsOut(amount_in, [WETH, USDC]).call()
    usdc_out = amounts[1] / 10**6

    print(f"💰 1 ETH = ${usdc_out:,.2f} USD")
    print(f"\n🎉 Real Ethereum price from Uniswap!")
    print(f"   (This is actual live data from mainnet)")

except Exception as e:
    print(f"❌ Error: {e}")

print("="*60)
