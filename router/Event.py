import os
from rx import Observable

class Event():
   """
      Event class definition
   """
   def __init__(self, eventData, eventType, eventSource):
      self.eventData = eventData
      self.eventType = eventType
      self.eventSource = eventSource
      self.eventId = hash(eventData)

   def __del__(self):
      print("event deleted")
      # @TODO send delete event to stack modules if needed
      # hadoop hdfs, plain file, db store, anlaytics
      return

   # Event utils
   def read(self, event):
      eventJson = {'publisher':'media'}
      return eventJson

   def write(self, ofile=os.getcwd()+'/logTraffic-event.json'):
      fo = open(ofile,'w')
      print("write log {0} in file {1}".format(self, ofile))
      return

   def augment(self, event):
      # enrich event data with score
      result = self.score(event)
      event[result.key] = result.value
      return event

   def translate(self, event, formula):
      # rewrite event into another event with a formula and delete the old one
      return event

   def readBid(self, bid, formula=None):
      event = bid
      return event

   def encrypt(self, event):
      # encrypt of event data
      return event

   def decrypt(self, event):
      # decrypt of event data
      return event

   def clear(self, event):
      # anonymize event data
      return event

   def score(self, event):
      # see augment result
      score = len(event)
      result = {'score' : score } # length/size of the data
      return result

   def filter(self, event, size, msgs=2):
      # min size of the event data
      source = Observable.of(event)

      source\
         .map(lambda s: len(s))\
         .filter(lambda i : i>=size)\
         .subscribe(lambda value : print(value)) # an observer is setup here with subscribe function

      # map associet une fonction/transforme fait une action
      # filter garde ce qu'on veut
      # subscribe c'est l'output en fonction d'un type d'events next, error, terminé

      # emits integer each 1000 ms
      # Observables can be created for button events, requests, timers, and even live Twitter feeds.
      Observable.interval(1000)\
         .map(lambda i : "{0} Mississipi".format(i))\
         .subscribe(lambda s : print(s))

      input("press any key to quit\n")

      from random import randint

      ''' use the rx events for the connection with the agent bidder class ?? '''
      three_emissions = Observable.range(1,msgs) # msg are separately sent to different subscribers
      three_random_ints = three_emissions.map(lambda i: randint(1,1000))
      three_random_ints.subscribe(lambda i: print("subscriber 1 received".format(i)))
      three_random_ints.subscribe(lambda i: print("subscriber 2 received".format(i)))

      # send the same message to different subscribers
      three_random_ints = three_emissions.mpa(lambda i: randint(1,1000)).publish()
      three_random_ints.subscribe(lambda i: print("subscriber 1 received".format(i)))
      three_random_ints.subscribe(lambda i: print("subscriber 1 received".format(i)))
      three_random_ints.connect()

      # .auto_connect(2) hold off until the number of subscriber reach 2
      # then  emissions is firing at this moment

      # Observable.zip(letters, intervals, lambda s, i: (s, i)) \ .subscribe(lambda t: print(t))


      '''
      save event SQL alchemy DB
      from sqlalchemy import create_engine, text
      from rx import Observable

      engine = create_engine('sqlite:///rexon_metals.db')
      conn = engine.connect()

      def customer_for_id(customer_id):
          stmt = text("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = :id")
          return Observable.from_(conn.execute(stmt, id=customer_id))

      # Query customers with IDs 1, 3, and 5
      Observable.of(1, 3, 5) \
          .flat_map(lambda id: customer_for_id(id)) \
          .subscribe(lambda r: print(r))
      '''
      return

      #def searchEvent():
      # use a key/data store to retrieve a specific event
      #  return
