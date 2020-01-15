from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLalchemy
from flask_marshmallow omport Marshmallow
from time import time
import os
import uuid

import auction # auction registry api import several functions defined in the auction core class ( bid_min_price    ,  timeout ^props,    strategy financial)

# see medium tutorial
# https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

import threading
class AsyncBidTask(threading.Thread):
   def __init__(self, task_id, params):
      self.task_id = task_id
      self.params = params
   def run():
      # --- send transaction to blockchain ---
      """ block_index = self.blockchain.frameworkConnector().sendTransaction(values['sellerId'],values['buyerId'],values['assetId'],values['price'])"""
      # import adBank
      # run Wallet.Debit() Credit() HashMessage() RecoverTransaction()

      # status = {'message': f'transaction will be added to block {index}'}
      # store the result in database for id = self.task_id
      bid = Bid.query.get(event_id)
      status = result_transaction_blockchain
      bid.status = status
      db.session.commit()

# --- Auction Entity Registry API ---
# 'timestamp' : time(),
# instantiate an app node
auctionRegistry_app = Flask(__name__)

# configuration SQLite  db
basedir = os.path.abspath(os.path.dirname(__file__))
auctionRegistry_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'example.db')

'''
usage = command line to create db in python comand line first time
from autionAPI import db
db.create_all()
-> as example.db is already created by the Ad Pipe, then it must work all together
'''
db = SQLAlchemy(auctionRegistry_app)
ma = Marshmallow(auctionRegistry_app)

# generate a globally unique address for this node
node_identifier = str(uuid.uuid4()).replace('-','')


# >>>> define assets model <<<<
class Asset(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   ext_id = db.Column(db.String(512), unique=False)
   content_url = db.Column(db.String(512), unique=True) # max size url, boring params with too much trackers params
   tracker_url = db.Column(db.String(512), unique=True)
   conversion_url = db.Column(db.String(512), unique=True)
   desc = db.Column(db.String(512), unique=False)
   is_active = db.Column(db.Integer, unique=False)
   block_id = db.Column(db.String(512), unique=False) # block id blockchain or false

   # XR experience fields will append next here size, quality, ratio, connection required, device required, experience type

   def __init__(self, ext_id, content_url, tracker_url=None, conversion_url=None, desc=None, is_active=0, block_id=0):
      self.ext_id = ext_id # external asset id
      self.content_url = content_url # display (cdn connector)
      self.tracker_url = tracker_url # see (ad server connector)
      self.conversion_url = conversion_url # fees plan + alert (crm connector) post-auction loop
      self.desc = desc
      self.is_active = is_active
      self.block_id = block_id

# define assets schema
class AssetSchema(ma.Schema):
   class Meta:
      # Fields to expose
      fields = ('ext_id', 'content_url', 'tracker_url', 'conversion_url', 'conversion_url', 'desc', 'is_active', 'block_id')

asset_schema = AssetSchema()
assets_schema = AssetSchema(many=True)

# define assets endpoint

# register a creative
@auctionRegistry_app.route('/asset/create', methods=['POST'])
def registerCreative():
   '''
   curl -X POST -H "Content-Type: application/json" -d '{ "assetId":"123", "description":"blabla", "creativeURL":"/assets/img/client2.png" }' "http://localhost:5000/assets/create"
   '''
   values = request.get_json()
   required = ['assetId','description','creativeURL']
   if not all(k in values for k in required):
      return 'missing values', 400

   # register the creative in the database
   new_creative = Asset(values['assetId'], values['creativeURL'])
   db.session.add(new_creative)
   db.session.commit()

   # --- blockchain connector develop here : ---
   # @TODO :
   #
   return jsonify(new_creative), 200

# show all assets
@auctionRegistry_app.route('/asset', methods=['GET'])
def get_asset():
   all_assets = Asset.query.all()
   result = assets_schema.dump(all_assets)
   # --- blockchain connector develop here : ---
   # @TODO :
   #
   return jsonify(result.data)

# get a creative by id
@auctionRegistry_app.route('/asset/<id>', methods=['GET'])
def asset_detail(id):
   creative = Asset.query.get(id)
      # --- blockchain connector develop here : ---
   # @TODO :
   #
   return asset_schema.jsonify(asset)

# update a creative (dictionnary)
@auctionRegistry_app.route('/asset/<id>', methods=['PUT'])
def asset_update(id):
   asset = Asset.query.get(id)
   ext_id = request.json['assetId']
   description = request.json['description']
   creative_url = request.json['creativeURL']
   asset.ext_id = ext_id
   asset.desc = description
   asset.content_url = creative_url
   # should not edit the blockchain
   db.session.commit()
   return asset_schema.jsonify(asset)

# delete a creative
@auctionRegistry_app.route('/asset/<id>', methods=['DELETE'])
def asset_delete(id):
   asset = Asset.query.get(id)
   db.session.delete(asset)
   db.session.commit()
   return asset_schema.jsonify(asset)

# @TODO :
@auctionRegistry_app.route('/asset/complain', methods=['POST'])
def acomplain():
   values = request.get_json()
   print(values)
   required = ['assetId','buyerId','description']
   if not all(k in values for k in required):
      return 'missing values', 400

   complain = self.blockchain.frameworkConnector().complain(values['assetId'])

   complain_hook = print('automated check')

   response = {
      'sellerId' : complain.sellerId,
      'buyerId' : complain.buyerId,
      'assetId' : complain.buyerId,
      'description' : complain.description
   }
   return jsonify(response), 200




# >>>> bid model <<<<
## direct feed by XRTB data flow
class Bid(db.Model):

   # ---* the consumer data *---
   geo = db.Column(db.String(128), unique=False) # geo sig ( ip + location )
   auth = db.Column(db.String(128), unique=False)
   ts = db.Column(db.String(128), unique=False)
   uid = db.Column(db.String(128), unique=False)
   ua = db.Column(db.String(512), unique=False)

   # ---* the app data *---
   event_id = db.Column(db.String(128), unique=False) # PK unique theoritically
   event_source = db.Column(db.String(128), unique=False) # px, player, partner
   event_score = db.Column(db.Real, unique=False)

   # ---* the supply data *---
   site_domain =db.Column(db.String(128), unique=False)
   site_page = db.Column(db.String(128), unique=False)
   site_topic = db.Column(db.String(128), unique=False)
   site_visual = db.Column(db.String(128), unique=False)
   site_is_XR = db.Column(db.Integer, unique=False)
   site_admin = db.Column(db.String(64), unique=False)

   # ---* the offchain transactional data *---
   bid_seller = db.Column(db.String(128), unique=False)
   bid_buyer = db.Column(db.String(128), unique=False)
   bid_min_price = db.Column(db.Real, unique=False)
   bid_price = db.Column(db.Real, unique=False)
   bid_index = db.Column(db.Integer, unique=False)

   # the data is physically on the hdfs source :
   # ar pixel, AdXRTBPipe, ar player
   def __init__(self):
      geo = "ip-coords"
      auth = "login" # cookie grap signature
      ts = "timestamp"
      uid = "cookie-id"
      ua = "user-agent"
      # -- user- data api can be used for the gdpr self-managed regulatory service
      event_id = "app-internal-event-id" # external ?
      event_source = "client-tracker-version/id"
      event_score = "client-tracker-opportunity-score"
      site_domain = "www.google.fr"
      site_page = "/homepage"
      site_visual = "features"
      site_is_XR = ""
      site_admin = "@" # header_bidding, smart_call, supply_file_index client strategy
      # --- site- data api can be use to automatize action with publishers
      bid_seller = "seller account id" # reject all others
      bid_buyer = "buyer account id" # reject all others
      bid_min_price = 0.02
      bid_price = None
      bid_index = 0


# define bid schema
class BidSchema(ma.Schema):
   class Meta:
      fields =  (bid_seller, bid_buyer, bid_min_price, bid_price, bid_index)

bid_schema = BidSchema()
bids_schema = BidSchema(many=True)

# the bid data feed doesnt use the API
# the trade flow update the bid event registry
# - duplicate bid transac for the fast performance opti and analytics
# - the blockchain doesnt suit for analytics mass data (cost is double indx? )

# define bid endpoint
# ---* place a bid (buyer ) *---
'''
the bid response API should use text format for Cython read/write
   - read the bid placed from any dsp
   - send the transaction to the blockchain and save status DB
   - after the auction timeout then update status into DB
https://cython.readthedocs.io/en/latest/src/tutorial/strings.html
https://stackoverflow.com/questions/37141696/how-to-send-asynchronous-request-using-flask-to-an-endpoint-with-small-timeout-s
'''

@auctionRegistry_app.route('/bid/place/<event_id>', methods=['POST'])
def placeBid(event_id): # duplicate GET/POST event_id
   values = request.get_json()
   # check that the required fields are in the post'ed data
   # required = ['sellerId', 'buyerId', 'assetId', 'price']
   required = ['seat', 'event_id', 'assetId', 'price'] # format +appnexys
   # ---* handle header authentication of the Buyer *---
   #
   if not all(k in values for k in required):
      return 'missing values', 400

   # async status codes: processing (started) , block index (done), error
   price = request.json['price']
   bid = Bid.query.get(event_id)
   bid.price = price # last bid price
   bid.status = "processing" # task id
   db.session.commit()

   async_task = AsyncBidTask(task_id=event_id, params=None)
   async_task.start()  # send transaction to blockchain
   task_status_url = url_for('task_status'), task_id=task_id)

   # update bid status with block index reference [ after auction timeout
   return bid_schema.jsonify(bid), 201 # return asset_schema.jsonify(asset)


# ---* reserve a bid (BETTER PRIO) *---
# use for direct deal with publisher or private auction
@auctionRegistry_app.route('/bids/reserve', methods=['POST'])
def reserve(event_id):
   values = request.get_json()
   required = ['seat', 'event_id', 'assetId', 'buy_price']
   if not all(k in values for k in required):
      return 'missing values', 400

   price = request.json['buy_price']
   bid = Bid.query.get(event_id)
   bid.price = price # last bid price
   bid.status = "processing" # task id
   db.session.commit()

   async_task = AsyncBidTask(task_id=event_id, params=None)
   async_task.start()  # send transaction to blockchain
   task_status_url = url_for('task_status'), task_id=task_id)

   # suggestion : should we force update of the bid status after the auction for this event has timeout to double-check ?
   return bid_schema.jsonify(bid), 201

# use event_id for task_id until a new table is created for tasks / bid placed async
@auctionRegistry_app.route('/bids/status/<int:task_id>', methods=['GET'])
def task_status(task_id):
   ## query bid status and return data
   """ TODO = need to create a new table with task_id instead of bid to not overload the bid event table with write from DSP and write from TRACKERS Pixels and AR player events """
   bid = Bid.query.get(event_id)
   return bid_schema.jsonify(bid), 201


# - blockchain withdraw
@auctionRegistry_app.route('/bids/withdrawal', methods=['POST'])
def withdraw():
   values = request.get_json()
   #check that the required fields are in the post'ed data
   required = ['sellerId', 'buyerId', 'assetId']
   if not all(k in values for k in required):
      return 'missing values', 400

   # TODO : and check index is effectively returned by framework ledger
   index = self.blockchain.frameworkConnector().sendTransaction(values['sellerId'],values['buyerId'],values['assetId'])

   response = {'message': f'transaction will be added to block {index}'}
   return jsonify(response), 201



# >>>> ---* User *--- <<<<
# define user model
''' Structure will be
      - Wallet > Account 1 > Vendor
      -        > Account 2 > Advertiser
      -        > Account 3 > User/Consumer
    The implementation is defined in AdBank package and integrate
    some utils inherited from the blockchain and beeswax masterbanker + RTB kit .
'''
# define user schema

# define user endpoint











# run app
   def server(self, auctionRegistry_app):
      self.auctionRegistry_app.run(host='0.0.0.0', port= 5000)



# Item/Asset
# transfer asset - immediate use-case to transfer a creative to another buyer/vendor/user : creative agency to put the creative content in the blockchain ?
@auctionRegistry_app.route('/assets/transfer', methods=['POST'])
def transfer(): # seller can give the bid to a buyer for free
   values = request.get_json()
   #check that the required fields are in the post'ed data
   required = ['sellerId', 'buyerId', 'assetId']
   if not all(k in values for k in required):
      return 'missing values', 400

   # TODO : check index is well returned by framework ledger
   index = self.blockchain.frameworkConnector().sendTransaction(values['sellerId'],values['buyerId'],values['assetId'])

   # TODO : and run the push content request here
   """ display content here """
   # get buyer creative URL
   r = requests.get(buyer, hooks={'response': [print_url, record_hook]})
   response = {'message': f'transaction will be added to block {index}'}
   return jsonify(response), 201

# Person/User
   @auctionRegistry_app.route('/users/complain', methods=['POST'])
   def ucomplain():
      values = request.get_json()
      # user Id can be a buyer, a seller or a consumer -
      required = ['userId','description']
      if not all(k in values for k in required):
         return 'missing values', 400

      complain = self.blockchain.frameworkConnector().complain(values['userId'])

      complain_hook = print('automated check')

      response = {
         'sellerId' : complain.sellerId,
         'buyerId' : complain.buyerId,
         'assetId' : complain.buyerId,
         'description' : complain.description
      }
      return jsonify(response), 200

