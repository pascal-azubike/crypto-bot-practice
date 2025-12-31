#!/usr/bin/env python3
"""
Wallet Generator for Crypto Trading Bot
========================================
This script creates a new Ethereum wallet for TESTNET use only.

⚠️ SECURITY WARNING:
- This wallet is for LEARNING purposes only
- Use ONLY on testnets (Sepolia, Mumbai, etc.)
- NEVER send real money to this wallet
- NEVER use this method for production/mainnet wallets

For production, use hardware wallets (Ledger, Trezor)
"""

from eth_account import Account
import secrets
import os
from pathlib import Path

def create_new_wallet():
    """
    Create a new Ethereum wallet
    Returns: account object with private key and address
    """
    # Generate random private key (32 bytes = 256 bits)
    private_key = "0x" + secrets.token_hex(32)

    # Create account from private key
    account = Account.from_key(private_key)

    return account, private_key


def display_wallet_info(account, private_key):
    """
    Display wallet information in a clear format
    """
    print("\n" + "="*70)
    print("🎉 NEW WALLET CREATED SUCCESSFULLY!")
    print("="*70)

    print("\n📍 WALLET ADDRESS:")
    print(f"   {account.address}")

    print("\n🔑 PRIVATE KEY:")
    print(f"   {private_key}")

    print("\n" + "="*70)
    print("⚠️  CRITICAL SECURITY REMINDERS:")
    print("="*70)
    print("1. This wallet is for TESTNET ONLY")
    print("2. NEVER send real money (mainnet tokens) to this address")
    print("3. NEVER share your private key with anyone")
    print("4. NEVER commit your .env file to GitHub")
    print("5. For production/mainnet, use a hardware wallet")
    print("="*70)


def save_to_env_file(account, private_key):
    """
    Offer to save credentials to .env file
    """
    print("\n📝 Would you like to save these to your .env file? (y/n): ", end="")
    choice = input().lower().strip()

    if choice == 'y' or choice == 'yes':
        env_path = Path('.env')

        if env_path.exists():
            # Read existing .env
            with open('.env', 'r') as f:
                lines = f.readlines()

            # Update or add wallet info
            updated = False
            for i, line in enumerate(lines):
                if line.startswith('PRIVATE_KEY='):
                    lines[i] = f'PRIVATE_KEY={private_key}\n'
                    updated = True
                elif line.startswith('WALLET_ADDRESS='):
                    lines[i] = f'WALLET_ADDRESS={account.address}\n'
                    updated = True

            # If not found, add them
            if not updated:
                lines.append(f'\n# Wallet (Created: {__import__("datetime").datetime.now()})\n')
                lines.append(f'PRIVATE_KEY={private_key}\n')
                lines.append(f'WALLET_ADDRESS={account.address}\n')

            # Write back
            with open('.env', 'w') as f:
                f.writelines(lines)

            print("✅ Wallet info saved to .env file!")
        else:
            print("❌ .env file not found in current directory")
            print("   Please create it first or save manually")
    else:
        print("\n📋 Copy these values manually to your .env file:")
        print(f"\nPRIVATE_KEY={private_key}")
        print(f"WALLET_ADDRESS={account.address}")


def get_faucet_links(address):
    """
    Display links to get testnet tokens
    """
    print("\n" + "="*70)
    print("💰 GET FREE TESTNET TOKENS")
    print("="*70)
    print("\nYour wallet address for faucets:")
    print(f"   {address}")

    print("\n🚰 Testnet Faucets:")
    print("\n1. Ethereum Sepolia:")
    print("   • https://sepoliafaucet.com/")
    print("   • https://www.alchemy.com/faucets/ethereum-sepolia")

    print("\n2. Base Sepolia:")
    print("   • https://www.alchemy.com/faucets/base-sepolia")

    print("\n3. Polygon Amoy:")
    print("   • https://www.alchemy.com/faucets/polygon-amoy")

    print("\n4. Arbitrum Sepolia:")
    print("   • https://www.alchemy.com/faucets/arbitrum-sepolia")

    print("\n5. BSC Testnet:")
    print("   • https://testnet.bnbchain.org/faucet-smart")

    print("\n💡 TIP: Visit each faucet and request tokens for testing!")
    print("   It takes 1-5 minutes to receive tokens.")
    print("="*70)


def main():
    """
    Main function to create wallet and guide user
    """
    print("\n🚀 CRYPTO TRADING BOT - WALLET GENERATOR")
    print("="*70)
    print("This will create a NEW wallet for testnet use.")
    print("="*70)

    # Check if web3 is installed
    try:
        from web3 import Web3
    except ImportError:
        print("\n❌ Error: web3 package not found")
        print("Please install it first: pip install web3")
        return

    # Create wallet
    print("\n🔄 Generating new wallet...")
    account, private_key = create_new_wallet()

    # Display info
    display_wallet_info(account, private_key)

    # Offer to save
    save_to_env_file(account, private_key)

    # Show faucet links
    get_faucet_links(account.address)

    print("\n✨ Setup complete! You're ready to start learning.")
    print("\n📚 Next steps:")
    print("   1. Get testnet tokens from the faucets above")
    print("   2. Verify your .env file has the wallet info")
    print("   3. Run test_connection.py to verify everything works")
    print("   4. Start Day 1 lessons!")

    print("\n" + "="*70)


if __name__ == "__main__":
    main()
