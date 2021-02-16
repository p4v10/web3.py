from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xc0977B80f61Eb6ccDB04aB1E180B1ba190B06471"
account_2 = "0x123cD500f7102Cb03c8A381C2e283EA4A52Ee188"

private_key = "316261d36367ac9a3cf9081f390666604c0c36230aa7f78f675190536e37ab28"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get transaction hash
print(web3.toHex(tx_hash))
