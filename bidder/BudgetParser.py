class BudgetPacer(object):
    def config(self, bank, amount, account):
        self.body = # config timely spend
        self.headers =
        self.url = # banker account balance and other measures to opt
        self.http_client =  AsyncHTTPClient() # async to not block the bidder
        return

    def getBudget(self):
        print("pacing bidder budget !")
        try:
            self.http_client.fetch(self.url,
                callback=handle_async_request,
                method='POST',
                headers=self.headers,
                body=self.body)
        except:
            print("pacing bidder budget failed !")

