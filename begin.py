from web3 import Web3

infura_url = "https://ropsten.infura.io/v3/ccb847f5a52f472ea9fb8fa0ae9b3af0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x989C33f6121281F8938feda41a24AE2c3306AD99")
print(web3.fromWei(balance, "ether"))