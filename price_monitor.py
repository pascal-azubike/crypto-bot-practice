
"""
REAL-TIME PRICE MONITOR
=======================
Monitors ETH price on Uniswap and alerts on changes
"""

from web3 import Web3
from dotenv import load_dotenv
import os
import time
from datetime import datetime

load_dotenv()

# Connect to mainnet
alchemy_key = os.getenv('ETHEREUM_RPC_URL').split('/')[-1]
MAINNET_RPC = f'https://eth-mainnet.g.alchemy.com/v2/{alchemy_key}'
w3 = Web3(Web3.HTTPProvider(MAINNET_RPC))

# Uniswap Router
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

# Tokens
WETH = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
USDC = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'

# Create contract
router = w3.eth.contract(address=UNISWAP_ROUTER, abi=ROUTER_ABI)

# Monitoring settings
CHECK_INTERVAL = 10  # seconds
ALERT_THRESHOLD = 0.5  # Alert if price changes by 0.5% or more

def get_eth_price():
    """Get current ETH price from Uniswap"""
    try:
        amount_in = w3.to_wei(1, 'ether')
        amounts = router.functions.getAmountsOut(amount_in, [WETH, USDC]).call()
        price = amounts[1] / 10**6
        return price
    except Exception as e:
        print(f"Error getting price: {e}")
        return None


def calculate_change(old_price, new_price):
    """Calculate percentage change"""
    if old_price == 0:
        return 0
    return ((new_price - old_price) / old_price) * 100


print("🔍 ETH PRICE MONITOR STARTING...")
print("="*60)
print(f"📊 Checking every {CHECK_INTERVAL} seconds")
print(f"🚨 Alert threshold: ±{ALERT_THRESHOLD}%")
print("="*60)
print("\nPress Ctrl+C to stop\n")

# Get initial price
previous_price = get_eth_price()

if previous_price is None:
    print("❌ Failed to get initial price")
    exit()

print(f"💰 Initial Price: ${previous_price:,.2f}")
print(f"⏰ Started at: {datetime.now().strftime('%H:%M:%S')}\n")

# Store price history
price_history = [previous_price]
check_count = 0

try:
    while True:
        # Wait before next check
        time.sleep(CHECK_INTERVAL)

        # Get new price
        current_price = get_eth_price()

        if current_price is None:
            continue

        check_count += 1
        price_history.append(current_price)

        # Calculate change
        change_percent = calculate_change(previous_price, current_price)
        change_amount = current_price - previous_price

        # Get current time
        now = datetime.now().strftime('%H:%M:%S')

        # Determine if alert needed
        if abs(change_percent) >= ALERT_THRESHOLD:
            # ALERT! Significant change
            emoji = "🚀" if change_percent > 0 else "📉"
            print(f"\n{emoji} ALERT! Price changed by {change_percent:+.2f}%")
            print(f"   Time: {now}")
            print(f"   Old Price: ${previous_price:,.2f}")
            print(f"   New Price: ${current_price:,.2f}")
            print(f"   Change: ${change_amount:+,.2f}\n")
        else:
            # Normal update
            emoji = "📈" if change_percent >= 0 else "📉"
            print(f"[{now}] {emoji} ${current_price:,.2f} ({change_percent:+.2f}%)")

        # Update for next iteration
        previous_price = current_price

        # Show summary every 10 checks
        if check_count % 10 == 0:
            highest = max(price_history)
            lowest = min(price_history)
            average = sum(price_history) / len(price_history)

            print(f"\n{'='*60}")
            print(f"📊 SUMMARY (Last {check_count} checks)")
            print(f"{'='*60}")
            print(f"   Current:  ${current_price:,.2f}")
            print(f"   Highest:  ${highest:,.2f}")
            print(f"   Lowest:   ${lowest:,.2f}")
            print(f"   Average:  ${average:,.2f}")
            print(f"   Range:    ${highest - lowest:,.2f}")
            print(f"{'='*60}\n")

except KeyboardInterrupt:
    print("\n\n🛑 Monitor stopped by user")
    print(f"📊 Final Statistics:")
    print(f"   Total checks: {check_count}")
    print(f"   Duration: {check_count * CHECK_INTERVAL} seconds")
    print(f"   Final price: ${current_price:,.2f}")
    print("\n✅ Session complete!")
