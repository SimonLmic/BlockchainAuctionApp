# built in
import requests

# import 3rd
from sanic import Sanic
from sanic.response import json
import web3

# import advertiser + banker wallet budget
import advertiser
import adBank

# import campaign modules
import campaign
import creative
import line
import flight

'''
router ->
   (HTTP / POST : OpenRTB / Request) ->
      BiddingAgent : { HttpServer -> Process OpenRTB JSON ->
         (HTTP / HEADER 200 : OpenRTB / Response) } ->
            router
'''

class AgentBidderHandler():

    def __init__(self):
        return

    def run():
        return

    def get():
        return

    def post():
        return

    def process_req():
        return

    def process_bid():
        return

class adServerHandler():
    def post(self):
        self.set_status(200)
        self.write("")
    def get(self):
        self.set_status(200)
        self.write("")

class AgentBidder(AgentBidder, Strategy):
    def __init__(self, application, request, **kwargs):
        super(AgentBidderHandler, self).__init__(application, request, **kwargs)
        if (self.bid_config is None):
            self.do_config()

    def process_bid(self, req):
        response = self.do_bid(req)
        return response

class Strategy():
    openRtb = OpenRtb_response()

    def do_config(self):
        return

    def do_bid(self, req):

        res = self.openRTB_get_default_response(req)
        #update price and creatives
        for bid in bids:
            # do something
            print("update bid response with  config")

        return res

def runBidder():

    # budget pacer start async update
    pacer = BudgetParser()
    pacer.config =((web3.banker, 7545), budget, account)
    # add a periodical event to call pacer
    PeriodicalCallback(pacer.http_request, period).start()

    # adserver start listen
    adserver_win = app( / ,  adServerHandler)
    # listen(port)
    adserver_event = app( / ,  adServerHandler)
    # listen(port)


    # tcp port bind

    # start app Flask / Sanic

    # start server and attach app Sanic to it

    # process request









