"""
DEX SIMULATOR - Understand How Uniswap Works
=============================================
"""

def calculate_price(reserve_token_out, reserve_token_in):
    """
    Basic Uniswap price formula
    """
    return reserve_token_out / reserve_token_in


def calculate_output_amount(amount_in, reserve_in, reserve_out):
    """
    Calculate how much you get when swapping
    Includes 0.3% fee
    """
    # Apply 0.3% fee (997/1000 = 99.7%)
    amount_in_with_fee = amount_in * 997

    # Constant product formula: x * y = k
    numerator = amount_in_with_fee * reserve_out
    denominator = (reserve_in * 1000) + amount_in_with_fee

    return numerator / denominator


print("🏊 UNISWAP LIQUIDITY POOL SIMULATOR")
print("="*60)

# Initial pool state
eth_reserve = 1000      # 1000 ETH in pool
usdc_reserve = 3_200_000  # 3.2M USDC in pool

print(f"\n📊 Initial Pool State:")
print(f"   ETH:  {eth_reserve:,}")
print(f"   USDC: ${usdc_reserve:,}")

# Calculate initial price
initial_price = calculate_price(usdc_reserve, eth_reserve)
print(f"\n💰 Initial Price: 1 ETH = ${initial_price:,.2f}")

# Simulate a BUY (swap USDC for ETH)
print("\n" + "="*60)
print("🔄 SIMULATION: Someone buys 10 ETH")
print("="*60)

buy_amount_eth = 10  # Want to buy 10 ETH

# Calculate how much USDC needed
usdc_needed = calculate_output_amount(buy_amount_eth, eth_reserve, usdc_reserve)

print(f"\n📍 Before Trade:")
print(f"   Pool ETH:  {eth_reserve:,.2f}")
print(f"   Pool USDC: ${usdc_reserve:,.2f}")
print(f"   Price: ${initial_price:,.2f} per ETH")

# Update pool reserves
eth_reserve -= buy_amount_eth
usdc_reserve += usdc_needed

# Calculate new price
new_price = calculate_price(usdc_reserve, eth_reserve)

print(f"\n📍 After Trade:")
print(f"   Pool ETH:  {eth_reserve:,.2f}")
print(f"   Pool USDC: ${usdc_reserve:,.2f}")
print(f"   Price: ${new_price:,.2f} per ETH")

# Calculate price impact
price_impact = ((new_price - initial_price) / initial_price) * 100

print(f"\n📈 Trade Impact:")
print(f"   USDC paid: ${usdc_needed:,.2f}")
print(f"   Effective price: ${usdc_needed/buy_amount_eth:,.2f} per ETH")
print(f"   Price impact: +{price_impact:.2f}%")

print("\n💡 Key Insight:")
print("   Large trades move the price!")
print("   This is called 'slippage'")
print("="*60)
