from web3 import Web3

infura_url = "wss://mainnet.infura.io/ws/v3/ccb847f5a52f472ea9fb8fa0ae9b3af0"

# Web3 Instance
web3 = Web3(Web3.HTTPProvider(infura_url))

# Create account
account = web3.eth.account.create()
print(account.address)

# Encrypt account
keystore = account.encrypt('pasha13')
print(keystore)

# Decrypt account
web3.eth.account.decrypt(keystore, 'pasha13')