import requests
from web3 import Web3

'''
    Blockchain wrapper abstract blockchain functions
'''

# blockchain wrapper
class BlockchainWrapper():

    def __init__(self, server='http://127.0.0.1', port='7545'):
        self.server = server
        self.port = port
        self.url = self.server + ':' + self.port
        self.web3 = Web3(Web3.HTTPProvider(self.url)) # request_kwargs
        # transaction_status = self.web3.txpool.inspect
        # https://ethereum.stackexchange.com/questions/24127/how-to-access-to-txpool-within-a-web3-script
        self.last_block = self.web3.eth.getBlock('latest')
        return

    def getConnector(self):
        return self.web3

    def setConnector(self, server, port, provider):
        self.server = server
        self.port = port
        self.url = server + ':' + port # build()
        self.web3 = provider
        return self.web3

    def getAllAccounts(self):
        jsonRPC_data = {"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}
        server = 'http://127.0.0.1'
        port = '7545'
        url = server + ':' + port
        r = requests.post(url, json=jsonRPC_data)
        accounts = r.text
        print(self.web3.eth.accounts)
        print(len(self.web3.eth.accounts))
        return accounts

    #  FAST contract eth.call READ local
    def call(self, transaction, block):
        self.web3.eth.call(transaction, block)
        return

    def lockAccount(self, account_hex):
        self.web3.personal.lockAccount(account_hex)
        return

    def unlockAccount(self, account_hex, passphrase):
        result = self.web3.personal.unlockAccount(account_hex, passphrase)
        return result

    # todo : see notes about IPC // RPC (inter process communication)
    def newAccount(self, passphrase):
        accounthex = self.web3.personal.newAccount(passphrase)
        return accounthex

    def getBalance(self, account_hex):
        balance = self.web3.eth.getBalance(account_hex)
        # last block balance
        last_block = self.web3.eth.getBlock('latest')
        last_block_hex = last_block['hash'].hex()
        last_balance = self.web3.eth.getBalance(account_hex, last_block_hex)
        return balance, last_balance

    def sendTransaction(self, seller, buyer, value):
        value_ETH = self.web3.toWei(value, 'ether')
        self.web3.eth.sendTransaction({'to':seller,'from':buyer,'value':value_ETH})
        return
