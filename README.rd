# Blockchain Auction app

The Blockchain Auction App is a program inspired by RTBKit
https://github.com/rtbkit/rtbkit/wiki/What-is-RTBkit%3F

The Blockchain Auction App  Exchange Connector  is receiving bid-request from HALOGEM middleware  each time  a user is connected on my website advertisement.

More details on target Architecture following:
https://github.com/rtbkit/rtbkit/wiki/Architecture


Blockchain Auction App has :
* an auction is running on top of blockchain ganache container
* a bidder with a user web component to place bids, setup an Agent Bidder and provide rest API
* a router mediating multiple bids between auction and HALOGEM middleware
* a store to show events statistics


How to install :
install and run Ganache, it will start automatically a blockchain
https://www.trufflesuite.com/ganache

python router/EventService.py
python router/EventClient.py
Bid winner send API Request to third-party Server with 3D product URL


Data types :
    - publisher tools for the website
    [ data stream, hdfs, api, socket.io, https]

    - event service
    [class : event service] [data : event json]

    - events
    [class : augment] [data : Event]

    - agent bidder place bid response
    [class : agent bidder] [data : Bid]

    - The bid winner send API Request to User browsing multiple websites
    [auction/router] [Requests : ]

