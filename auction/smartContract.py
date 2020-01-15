from solc import compile_source
from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract

"""
  Smart contract is using criterias including Object3D position, rotation and size to provide the min price floor for the bid

"""


# Solidity source code ^0.4.22;

contract_source_code = '''
pragma solidity ^0.4.0;

contract SimpleAuction {
    // params of the auction. time are either
    // absolute unix ts or time periods in seconds.
    address public beneficiary;
    uint public auctionEnd;

    // Current state of the auction.
    address public highestBidder;
    uint public highestBid;

    // Allowed withdrawals of previous bids
    mapping(address => uint) pendingReturns;

    // Set to true at the the end, disallows any change
    bool ended;

    // Events that will be fired on changes.
    event HighestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

    // The following is a so-called natspec comment,
    // recognizable by the three slashes.
    // It will be shown when the user is asked to
    // confirm a transaction.

    /// Create a simple auction with `_biddingTime`
    /// seconds bidding time on behalf of the
    /// beneficiary address `_beneficiary`.
    constructor(
        uint _biddingTime,
        address _beneficiary
    ) public {
        beneficiary = _beneficiary;
        auctionEnd = now + _biddingTime;
    }

    /// Bid on the auction with the value sent
    /// together with this transaction.
    /// The value will only be refunded if the
    /// auction is not won.
    function bid() public payable {
        // payable keyword enable ETH transaction
        // no args as all informations are in the transaction itself

        // revert the call if the bidding
        // period is over / auction timeout
        require(
            now <= auctionEnd,
            "Auction already ended."
        );

        // if the bid is not higher, send the
        // money back
        require(
            msg.value > highestBid,
            "There already is a higher bid."
        );

        if (highestBid != 0) {
            // recipient have to withdraw their money
            // client-side
            pendingReturns[highestBidder] += highestBid;
        }
        highestBidder = msg.sender;
        highestBid = msg.value;
        emit HighestBidIncreased(msg.sender, msg.value);
    }

    function bidsimon(string _bid) constant returns (string) {
        return _bid;
    }

    /// withdraw a bid that was overbid.
    function withdraw() public returns (bool) {
        uint amount = pendingReturns[msg.sender];
        if (amount > 0) {
            pendingReturns[msg.sender]=0;
            if (!msg.sender.send(amount)) {
                pendingReturns[msg.sender]=amount;
                return false;
            }
        }
        return true;
    }

    function status() view public returns (uint) {
        return highestBid;
    }

    /// End the auction and send the highest bid
    /// to the beficiary.
    function auctionEnd() public {
        // 1. check conditions
        // 2. run actions
        // 3. interact with third-partie/S contracts
        // any mix up will cause potential integrity auction defects with payout risk mess-up

        // 1. conditions
        require(now >= auctionEnd, "Auction not yet ended.");
        require(!ended, "auctionEnd has already been called.");

        // 2. run actions
        ended = true;
        emit AuctionEnded(highestBidder, highestBid);

        // 3. interact
        beneficiary.transfer(highestBid);
    }
}

'''

def deploy_contract():
    compiled_sol = compile_source(contract_source_code) # compiled source code

    contract_interface = compiled_sol['<stdin>:SimpleAuction']

    # web3.py instance
    #web3 = Web3(TestRPCProvider())
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

    # set pre-funded account as sender
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # instantiate and deploy contract to blockchain
    SimpleAuction = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # submit the transaction that deploys the contract
    tx_hash = SimpleAuction.constructor(100, web3.eth.defaultAccount).transact()

    # get tx receipt to get contract address
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    # create the contract instance with the newly deployed address
    simple_auction = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=contract_interface['abi'],
        ContractFactoryClass=ConciseContract
    )
    return (SimpleAuction, tx_receipt.contractAddress, simple_auction)


# a bid transaction is providing Object3D spatial position in xyz coordonates, rotation and scale.
def do_bid():
    # print('bid: {}'.format(simple_auction.bid()))
    SimpleAuction.functions.bid().transact({'to': tx_receipt.contractAddress, 'from': web3.eth.defaultAccount, 'value': web3.toWei(0.00001, 'ether')})

    print('highestBid bid: {}'.format(simple_auction.status()))

