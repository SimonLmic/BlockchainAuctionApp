import time
import uuid
import requests

from flask import Flask, jsonify, request
import numpy as np

import auction.blockchainWrapper as bw
import router.Router as mr
import auction.BidderInterface as auction_bi

'''
    Define different Auction and their rules
'''

class Auction():
   # view on the inventory last hour
   # auction waterfall
   # view on the auction status
   def viewAllStats():
      return True


class PrivateAuction(Auction):
   # 3D/XR auction is
   # header bidding (RTB +)
   # direct orders (Private market place)
   # RTB
   # fallback
   #  -> open to other DSP my ad network ?

   # waterfall bid pipeline (learn from headerbidding, direct orders ,RTB , fallback)
   def viewPrivateStats():
      return True


class Bid(object):
   def factory(type):
      if type == 'event' : return object()
      if type == 'BidEvent' : return BidEvent()
      assert 0, 'bad shape creation: ' + type
   factory = staticmethod(factory)

class BidEvent(Bid):
   def __init__(self):
      self.bid_price = 0.00
      self.vendor = 'publisher_id'
      self.active = False
      self.bidProbability = 1
      self.blockchain_id = 'blockchain'
      return

   def filter(self, escrow):
      err = None
      if self.vendor in escrow or self.bidProbability < 0:
         # TODO count escrow level and decide to delete
         del(self)
      return err

   def price(self, bidPrice):
      err = None
      self.bid_price = bidPrice
      return err

   def blockchain(self, blockchainId):
      err = None
      self.blockchain_id = blockchainId
      return err

   # init & deploy smartcontract
   def contract(self, blockchain):
      err = None
      import auction.smartContract as sc
      simple_auction_contract, contract_address, concise_contract = sc.deploy_contract()
      print(simple_auction_contract, contract_address, concise_contract)
      return simple_auction_contract, contract_address, concise_contract

   # prepare bid request
   def prepare(self, formula=None):
      err = None
      assert type(self.bid_price) is np.float32, "not a float number : %r type %r" %(self.bid_price, type(self.bid_price))
      assert self.bid_price <= 0, "negative price : %r" % self.bid_price
      if self.bidProbability < 0.5 :
         self.active = False
      else :
         self.active = True
      return err

   def show(self):
      print(self,type(self))
      return self

   def fallback(self):
      del(self)
      return

   def log(self, dbwrap, bwrap):
      """
      IPFS distributed hash table to store the data in blockchain
      COUPLED with centralized APP db event.
      """
      # save this event in SQL db
      # update auction params : init, ready, closed, timeout
      return



class Augmentor():
   """
      The Augmentor add more content (tags, topics, 3rd) in the bid request data in order to optimize the decisions made by the agent bidder
   """
   def __init__():
      return


class BidRequests_Parser():
   """
      The Events are received from the 3D/XR Advertising Experience
      depending on program version
   """
   def __init__():
      return




class PodAuction(Auction):
   """
      Pod Auction class
      - input : read the inventory from received events
      - active : run the auction and send the bids requests to bidders
   """
   def __init__(self):
      # general bid auction settings
      self.auction_time_left = 10 # bid timeout
      self.auction_bid_stategy = self.perf_bid_strategy1 # bid min price
      bwrap = bw.BlockchainWrapper() # connector to the already blockchain
      self.blockchain = bwrap
      self.router = mr.Router() # auction router
      self.router_advertiser = 'xrtb pip ' # event service router
      return

   def setRouter(self,router_xrtb):
      self.router_advertiser = router_xrtb
      return

   def on_auction_closure(self, bid, auction_delta):
      import syslog
      syslog.syslog('got a bid win !')
      self.router_advertiser.advertiser(bid) # translate win bid into event
      return

   # Matching Engine []
   def nicerBid1(self, bidEvent):
      # match bid with buyer shortlist
      # optimize matching performance
      return bidEvent

   # TODO perf fix
   def perf_bid_strategy1(self, bid_price, bid_index):
      # tier depends on previous bids number [ + % popularity ? ]
      y = np.log10(bid_index)
      # then compute bid min price
      min_bid_price = y*bid_price
      # strategy plot viz
      import matplotlib.pyplot as plt
      x = np.linspace(0, 10)
      y = np.log10(x)
      plt.plot(x,y)
      plt.show()
      return min_bid_price

   def setMinBidPrice(self):
      # token value, buyer shortlist size,
      # require a smart contract function condition update
      # one blokchain and smart contract per brand campaign
      self.token_price = 0.01
      min_bid_price = self.perf_bid_strategy1(bid_price, bid_index)
      return min_bid_price

   def translate(self, event):
      """
      translate a user event into a bid opportunity
      at the auction level :
         - register the bid in the auction
         - optimize the bid with a buyer shortlist
           :param event: <dict>
           :return bid: <dict>
      """
      err = None
      types = Bid.__subclasses__()
      bidevent_type = types[0].__name__
      bidevent_instance = Bid.factory(bidevent_type) # add new event source

      bid = bidevent_instance
      err = bid.filter("escrow")
      err = bid.price(np.float32(0))
      import uuid
      blockchainId= uuid.uuid4().hex
      err = bid.blockchain(blockchainId)

      # deploy smart contract
      t_deploy_start = time.perf_counter()
      simple_auction_contract, simple_auction_contract_address, concise_contract = bid.contract(blockchainId) # or contract adress ?

      bid = self.nicerBid1(bid) # bid optimization
      err = bid.prepare() # validate bid is well-formed before sending

      # bidder_interface = auction_bi.BidderInterface()
      auctionId = "first"
      bidders = "fake_bidresponse"
      timeLeft = "ms"

      # send bid
      t_send_bid_start = time.perf_counter()
      err = self.router.bidder_interface.sendBid(auctionId, bidders, bid, timeLeft)

      # receive response
      t_get_response_start = time.perf_counter()
      err = self.router.bidder_interface.sendBidResponse(auctionId, 'mydsp', 'openRtb_Response',simple_auction_contract, simple_auction_contract_address, concise_contract)

      t_get_response_stop = time.perf_counter()
      auction_delta = t_get_response_stop - t_deploy_start

      print(auction_delta, self.auction_time_left)
      if (auction_delta) < self.auction_time_left :
         self.on_auction_closure('openRtb_Response', auction_delta)
      else :
         print("auction timeleft exceed - No display !! ")

      # cost optimizations when bids are unsold, shared, deal and eventually log the bid for analytics
      bid.fallback()
      # on bid auction close call self-destruct
      # https://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html#self-destruct
      print("print bid", bid)
      return err

   def cleanAuction():
      # remove escrow seller bids with too many complains
      # remove old bids
      return


class Filter():
   """
      filters utils for bids
   """
   def __init__():
      return


class DataLogger():
   """
      analyics and logging
   """
   def __init__():
      return


class AdserverConnector():
   """
      receive win, impression, click and convert publisher notification
   """
   def __init__():
      return

