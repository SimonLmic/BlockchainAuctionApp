# python packages
import requests
import os, sys, csv, gzip, json
import threading
# from threading import Barrier

# external packages
import ujson

# application packages
sys.path.append('.')
from auction import blockchainWrapper, auctionEngine, adBank
from router import Router, Event, EventService

from store import Inventory


'''
    EventClient example:
    start blockchain auction
    generate simple publisher event instead of receiving from middleware
    send a request to  middleware
'''


def client():
   bwrap = blockchainWrapper.BlockchainWrapper()

   # generate account
   accounts_gen = ["Account"]
   accounts = [adBank.User.factory(account, bwrap) for account in accounts_gen]

   # show accounts
   for account in accounts:
      account.show()

   # blockchain auction init
   my_auction = auctionEngine.PodAuction()
   auction_vec = [my_auction]

   # ETL pipeline
   router = Router.AdXRTBPipe(auction_vec)
   my_auction.setRouter(router) # @fix reciproc tricky init

   # create event
   event = router.readCSVEventFile()
   eventType = 'publisherEvent'
   eventSource = 'arplayer'
   event = Event.Event(event, eventType, eventSource)

   # run auction
   router.runEvent(event)

   # after event is run, recheck account balance
   for account in accounts:
      account.getBalance(bwrap)

   # show some inventory analalytics
   inventory = Inventory.InventoryStore()
   inventory.view()
   inventory.top()



if __name__ == "__main__":
   thread = threading.Thread(target=client)
   thread.start()
