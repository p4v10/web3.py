from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/ccb847f5a52f472ea9fb8fa0ae9b3af0"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Getting Latest block  
latest = web3.eth.blockNumber
print(latest)

# Getting Latest block Information
print(web3.eth.getBlock(latest))

# Getting Latest 10 Blocks
for i in range(0,10):
    print(web3.eth.getBlock(latest - i))

hash = "0x078d00f3bc873e79f4271bbcb7faec7e8deb8c4a6d0c400da105f5e93066fff6"
print(web3.eth.getTransactionByBlock(hash, 2))