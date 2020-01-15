


# the bidder proxy class will handle all bid response
# from my bidder , internal auction and other DSP
# use RTB kit wrapper
class bidderProxy():

   # bid request API,
   def bidRequest():
      return
   # respondBid() - RTB kit - let my DSP place bids and other DSP
   def bidResponse():
      return



# token auction API
# add credit to account
def tokenProxy(account, wallet):
   return True

def increase():
   return True

def decrease():
   return True

def recycle():
   return True

def allocate():
   return True

def commit():
   return True

def adjust():
   return True

# duplicate and translate account operation into the blockchain request
# blocks - blockchain


# link/authenticate Account to blockchain identity( uport)


# wallet publisher - support master banker RTB KIT as soon as possible
# wallet advertiser - support master banker RTB KIT as soon as possible
def createWallet(account="",type="publisher"): # or advertising
   '''
   {
      "md" : {"objectType": "Account";
              "version": 1},
      "type": account type ("budget" or "spent")
      "budgetIncreases": amount (in USD/1M),
      "budgetDecreases": amount (in USD/1M),
      "spent": amount (in USD/1M),
      "recycledIn": amount (in USD/1M),
      "recycledOut": amount (in USD/1M),
      "allocatedIn": amount (in USD/1M),
      "allocatedOut": amount (in USD/1M),
      "commitmentsMade": amount (in USD/1M),
      "commitmentsRetired": amount (in USD/1M),
      "adjustmentsIn": amount (in USD/1M),
      "adjustmentsOut": amount (in USD/1M),
      "lineItems": additional keyed amounts,
      "adjustmentLineItems": additional keyed amounts
   }
   '''
   return True


