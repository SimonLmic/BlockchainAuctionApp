import os

import requests
import ujson
import uuid

import router.Event as me
import auction.adBank as ab
import auction.BidderInterface as auction_bi




class Router():
   """
      The Router class provide all functions to
      control the event processing :
         -  router receive events and filter
         -  transform events to a bid request
         -  send bid request to a bidder see PodAuction, Bid, Bidder
         -  match bid request with bid_placed=bid_response
         -  send content information for XR Advertising Experience
         -  simple alert
         - ensure real time
         - guarantees we do not ovespend

      the router mediate stuck events and redirect to address sender/recipients
      clean() requeue() detect() remove() redirect() queue() send()
      at different stack where are stored the events, bids and bid response
      input : events
      output : events

      options for auction, adBank, max spend, log bid+auction, analytics, slow
   """
   def __init__(self):
      # make configs for auction , bidder, from json
      #augmentation spent windows stat
      # set max/min
      #  set instance
      # init http bidder interfface
      self.bidder_interface = auction_bi.BidderInterface()
      # store publisher data
      # banker tracking
      # init auciton/X
      # init filters
      # bind protocol

      return
   def do_options():
      # set number of seconds after whuch a loss is assumed
      # set max bid price
      # set no bid probality  preprocessing
      # set augmentor timeout
      # set bank debug tracking
      # send data for publisher analytics
      # set exchange, bidder, filter, analytics configuration file
      # do slow mode
      return
   def start():
      # slave banker start
      # router start
      return
   def shutdown():
      return
   def maint():
      # route rinstance
      # router init and start
      # router for all exhcange enable
      # stats show
      return




class AdXRTBPipe():
   """
      The AD XRTB pipe class can
         - read/write in data logger
         - process/stop/run/restart events datastream
         - publisher store
         - user store
         - advertiser store

   """
   def __init__(self, auction_vec):
      self.publisher_wallet = ab.PublisherWallet()
      self.advertiser_wallet = ab.AdvertiserWallet()
      self.user_wallet = ab.UserWallet()
      self.bidder_wallet = ab.BidderWallet()
      self.auction_vec = auction_vec[0] # my decentralized auction

   # --- ADAPTER ---
   def readCSVEventFile(self):
      currentPath = os.getcwd()
      currentFile = currentPath+'/logTraffic.json'

      with open(currentFile) as f: # use control layer block
         #event_props = ['publisher','user','page','ad','context']
         event = f.read()
         # f.readline() read next line of the file foreach call
         # json.load(f) will load the json from the file
      event = ujson.loads(event)
      print("read file event : {} type : {}".format(event, type(event)))
      return event

   # --- EVENT PROCESS ---
   def runEvent(self, event):
      # @TODO : import multiprocessing
      # https://wiki.python.org/moin/GlobalInterpreterLock
      # reactivex
      if event.eventType is 'publisherEvent':
         self.publisher(event.eventData) # publisher updates
      elif event.eventType is 'advertiserEvent':
         self.advertiser(event.eventData)
      elif event.eventType is 'bidEvent':
         self.bidder(event.eventData) # receive a bid from a supply and respond
      else :
         self.fallback(event.eventData) # other events
         print(event.eventData)
      return

   def publisher(self, event):
      # save publisher event logs in the auction blockchain
      # using an auction blockchain framework adaptater/connector
      # add event value/volume norm score

      # translate an event into a bid opportunity
      event = ujson.loads(event)
      print(event, type(event))

      event['placement_id'] = '12321'
      if (event['placement_id']):
         bid = self.auction_vec.translate(event)
         print("hash ",bid)
      else :
         self.fallback(event)

      self.publisher_wallet.credit_trafficSQlite(event)
      self.publisher_wallet.debit_campaignSQlite(event)
      self.publisher_wallet.reportView()
      self.connect(event) # save user tracking data in DMP tables
      return

   def advertiser(self, bid):
      # display()
      event = self.translateBid(bid)

      creativePath = 'assets/models/products/DE-LEB-21c.gltf'

      # server = 'http://127.0.0.1:3000/'
      server = 'https://Simon-Laptop.local:443/'
      payload = {'creativeURL':server+creativePath,'cookieId': str(uuid.uuid4().hex),'headlines':["be here. in this. clawing back to self. scrupulous skin feeder. put on. give up. pay out.", "Leon Emanuel Blanck rejects traditional pattern making in favor of his own technique called ANFRACTUOUS DISTORTION","In an industry where the tactile connection between the garments and the creator seems to vanish, he has revived the craftsmanship by constructing anatomical patterns that are meticulously merged together. Each garment is constructed by hand and then goes through a deconstruction process.", "(415) 391-5550 | 317 Sutter Street San Francisco, California 94108","text1", "text2","text3" ]} # validate valid json
      # use targeting data to setup the correct event format depending on consumer client player
      # player_config = do_config(player.version())

      # send the event to the eventService interface
      url = 'http://127.0.0.1:8777/display/'
      r = requests.post( url, json=payload )
      print(r.text)
      # campaign()
      # line()
      # creative()
      # debit()
      # wait adserver connector notification
      return

   def translateBid(self, bid):
      event = me.Event(None, None, None)
      event.readBid(bid) # event to bid -- bid to event
      return event

   def fallback(self, event):
      # filtered events, events no bid
      return


   def initQueue():
      return queue

   def addEvent(queue):
      return loc

   def removeEvent(queue):
      return err

   def readQueue(queue):
      return action

   def showQueue(queue):
      return

   def operationQueue(self, queue, selector, action):
      return

   def move(self, interface):
      return err

   def batchMove(interface,events=[]):
      return err


   # as a router selector i want to detect when an event is log but not exist in auction view

   # as a router selector i want to detect when a win bid didn't not received ad server confirmation

   # as a router selector i want to detect when a win bid didn't received my tracker impression feedback



   # --- DATA (DMP) LOGGER LOAD ---
   def connect(self, event):
      # update publisher inventory (page rank, topic, specs, metatitle)
      # update publisher account (token, site, domain )
      # update user profile store (UPS)
      # update user history store (UHS)
      return

   def active(): # better user event with score() function ?.
      return

   def sync():
      # resync offline user data # analyse # batch # update
      return
