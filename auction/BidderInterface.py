class BidderInterface():
   '''
      configuration interface to specify router, bidder and adserver endpoints
   '''
   def __init__(self):
      return

   def sendAuctionMessage():
      return

   def sendBidLostMessage():
      return

   def sendBidInvalidMessage():
      return

   def sendNoBudgetMessage():
      return

   def sendMessage():
      return

   def sendErrorMessage():
      return

   def sendPingMessage():
      return

   def parseFormat():
      return

   def print_url(r, *args, **kwargs):
      print(r.url)

   def record_hook(r, *args, **kwargs):
      r.hook_called = True
      return r

   # batch all bid requests with router
   def batchSend(self, bid_vec, buyer_vec):
      for buyer in buyer_vec :
         r = requests.get(buyer, hooks={'response': [print_url, record_hook]})
      return

   def sendBid(self, auctionId, buyers, bid, timeLeft):
      if bid.active == True:
         # send to external bidder Cython text file /parser
         # send to internal agent bidder /
         print("always blue, always blue, always blue")
      return

   def sendBidResponse(self, auctionId, buyer, bid, contract, contractAddress, conciseContract):
      from web3 import Web3, HTTPProvider
      web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
      web3.eth.defaultAccount = web3.eth.accounts[0]
      buyer = web3.eth.defaultAccount

      contract.functions.bid().transact({'to': contractAddress, 'from': buyer, 'value': web3.toWei(0.00001, 'ether')})
      print('highestBid bid: {}'.format(conciseContract.status()))
      return
