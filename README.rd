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
https://www.trufflesuite.com/ganache use version 1.2.2 

Install Ganache 1.2.2 
Install python 3.6
pip install virtualenv
cd BlockchainAuctionApp
virtualenv --python= <path to python3.6>  <virtual env path>
source venv36/bin/activate
pip install requests
pip install flask
pip install numpy
pip install rx
pip install pandas
pip install 'sanic==0.7.0'
pip install 'web3==4.7.1'
pip install 'py-solc=3.1.0'


python router/EventService.py
python router/EventClient.py
Bid winner send API Request to third-party Server with 3D product URL

when running python EventClient.py a database is saved in example.db 

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

