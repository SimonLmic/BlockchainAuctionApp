import requests
from web3 import Web3
import auction.blockchainWrapper
'''
    adBank provides Blockchain Auction App User
        Accounts  and Wallets

    Ganache Json RPC endpoint :
    - https://github.com/trufflesuite/ganache
    - eth_sendtransaction :
    https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendtransaction
    - eth_getBalance :
    https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getbalance
'''
# or my blockchain testing endpoint
''' endpoint [localhost]/transactions/new '''


class User(object):
    # Create based on class name:
    def factory(type, bwrap):
        if type == "Account" :
            account = Account('ADCHERRY', 'ADCHERRY')
            # setup with connector
            accounthex = bwrap.newAccount(account.account_name)
            account.setAccountHex(accounthex)
            return account

        if type == "Advertiser":
            advertiser = Advertiser()
            return advertiser

        assert 0, "bas user creation : " + type
    factory = staticmethod(factory)


# ---* Accounts parent class *---
class Account(User):
    def __init__(self, passphrase, name):
        self.account_hex = None
        self.account_name = name
        self.account_token = 'ETH'

    def setAccountHex(self, account_hex):
        self.account_hex = account_hex
        return

    def show(self):
        attrs = vars(self)
        print(','.join("%s: %s" % item for item in attrs.items()))
        return

    def getBalance(self, bwrap):
        balance = bwrap.getBalance(self.account_hex)
        print(balance)
        return balance


class Advertiser(Account):
    # https://docs.beeswax.com/docs/testinput-1
    def __init__(self):
        super().__init__()
        self.advertiser_ext_id = '123'
        self.default_currency = 'USD'
        self.conversion_method_id = 1 # last click
        self.notes = ''
        self.active = True
        return


class Publisher(Account):
    def __init__(self):
        super().__init__()
        self.publisher_ext_id = '456'
        self.domain_name = 'lemonde.fr'
        self.notes = ''
        active = True
        return


class Consumer(Account):
    def __init__(self):
        super().__init__()
        self.provider = '' # post-buy service (loyalty/attrib)
        self.email = ''
        self.gender = ''
        self.geo = '' # geo-location
        self.active = bool(True)
        self.score = float(0.9)
        self.graph = ['cookie_cluster_id']
        self.words = ''
        return

class BUser(): # for GUI with role, permission
    def __init__(self):
        super().__init__()
        return


class Wallet():
    def __init__(self):
        self.account_id = '123'
        # Banker JSON API
        # POST /v1/accounts
        # This command is used to create a new account in the Banker database.
        # https://github.com/rtbkit/rtbkit/wiki/Banker-JSON-API
        self.event_value = '0.01'
        self.market_rate = '1'
        self.currency = 'token' # list of token , tree-account structur
        import sqlite3
        conn = sqlite3.connect('example.db')

    def credit():
        return

    def debit():
        return

    def show():
        return

class PublisherWallet(Wallet):
    def __init__(self):
        super().__init__()
        self.initPublisherDB()

    def credit_traffic(self, event_value):
        return

    def credit_trafficSQlite(self,event_value):
        # commit transaction database
        import sqlite3
        conn = sqlite3.connect("example.db")
        c = conn.cursor()
        print("before transaction sqlite ")
        credits = [(self.account_id,'BUY',self.event_value,self.market_rate,self.currency),]
        c.executemany('INSERT INTO publisher_stocks VALUES (?,?,?,?,?)', credits)
        conn.commit()
        for row in c.execute('SELECT * FROM publisher_stocks ORDER BY account'):
            print("records : ",row)
        conn.close()
        print("after transaction sqlite ")
        # version Banker-Database
        # This is a description of the data format used by the Banker process to store its value in its Redis database.
        # https://github.com/rtbkit/rtbkit/wiki/Banker-Database
        return

    def initPublisherDB(self):
        import sqlite3
        conn = sqlite3.connect("example.db")
        c = conn.cursor()
        # DEFINE MODEL HERE :
        # date, description, operation, values, analytics
        c.execute('''CREATE TABLE publisher_stocks
            (account real, trans text, price real, rate real, currency text)''')
        conn.commit()
        conn.close()
        return

    def cashflowToken():
        # https://github.com/rtbkit/rtbkit/wiki/Cash-flow-steps
        return

    def debit_campaign():
        return

    def debit_campaignSQlite(self, event_value):
        # commit transaction database
        import sqlite3
        conn = sqlite3.connect("example.db")
        c = conn.cursor()
        print("before transaction sqlite ")
        debits = [(self.account_id, 'SELL', self.event_value,self.market_rate,self.currency),]
        c.executemany('INSERT INTO publisher_stocks VALUES (?,?,?,?,?)', debits)
        conn.commit()
        for row in c.execute('SELECT * FROM publisher_stocks ORDER BY account'):
            print("records : ",row)
        conn.close()
        print("after transaction sqlite ")
        return

    def reportView(self):
        import sqlite3
        conn = sqlite3.connect("example.db")
        c = conn.cursor()
        # SQL request to show aggregated view on the stocks
        t = ('BUY',)
        c.execute("SELECT SUM(price) FROM publisher_stocks WHERE trans=?",t)
        totalbuy = c.fetchone()[0]
        print("BUY :", totalbuy)
        t = ('SELL',)
        c.execute("SELECT SUM(price) FROM publisher_stocks WHERE trans=?",t)
        totalsales = c.fetchone()[0]
        print("SELL :",totalsales)
        print("balance : ", totalbuy - totalsales)
        return

class AdvertiserWallet(Wallet):
    def credit_unsold(): # campaign unsold budget
        return

    def debit_campaign():
        return


class UserWallet(Wallet):
    def credit_loyalty_point():
        return

    def debit_service():
        return



class BidderWallet(Wallet):

    def agent():
        # Bidding agent
        # https://github.com/rtbkit/rtbkit/wiki/How-to-write-a-bidding-agent-using-Python-and-HTTP-API
        # https://github.com/rtbkit/rtbkit/wiki/Bidding-agent
        # https://github.com/rtbkit/rtbkit/blob/master/rtbkit/plugins/bidding_agent/bidding_agent.cc
        # config https://github.com/rtbkit/rtbkit/wiki/Agent-Configuration-Details
        return
    def credit():
        return

    def debit():
        return

    def integrationRTB():
        return
