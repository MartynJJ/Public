
class Asset:
    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_list = {
            "bfx" : 0,
            "gdax" : 0,
            "blockchain_info" : 0
            }
        self.API = API_Caller("url here")
    def total_balance(self):
        total = 0
        for key,value in self.balance_list.items():
            total += float(value)
        return total
    def balance_input(self, key = None):
        print("%s Balances:" % (self.symbol))
        if key == None:
            for key,val in self.balance_list.items():
                balance = float(raw_input("Balance in %s: " % key))
                self.balance_list[key] = balance
        else:
            self.balance_list[key] = float(raw_input("Intput balance for %s: " % (key)))
    def balance_detail(self):
        print("%s Balance Detail:" % (self.symbol))
        for key,value in self.balance_list.items():
            print("%s : %f" % (key, value))
    def asset_price(self, base = "USD"):
        price = self.API.price_call(self.symbol, base) 
        return (price)
    def asset_value(self, base = "USD"):
        return (self.total_balance() * self.asset_price(base))

class API_Caller:
    def __init__(self, url):
        self.url = url
    def price_call(self, symbol, base):
        #API call  here
        price = 0.05
        return price
        
class Wallet:
    def __init__(self, name="Default", base = " USD"):
        self.holdings = {}
        self.name = name
        self.default_base = base
    def add_asset(self, symbol):
        asset = Asset(symbol)
        self.holdings[asset.symbol] = asset
    def wallet_value(self):
        balance = 0
        for symbol,asset in self.holdings.items(): 
            balance += asset.asset_value()
            return balance
    def wallet_detail(self):
        detail = {}
        for symbol,asset in self.holdings.items(): 
                detail[symbol] = asset.total_balance()
        return detail
    def print_wallet_detail(self):
        detail = self.wallet_detail()
        print("Balance detail for %s wallet" % (self.name))
        for symbol,balance in detail.items():
            print("%s : %s" % (symbol, balance))
        
#Function testings  
'''          
mine = Asset('MNN')
mine.balance_input()
print(mine.total_balance())
mine.balance_input("bmx")
mine.balance_detail()
print(mine.asset_value())
'''

my_wallet = Wallet()

my_wallet.add_asset("MNN")
my_wallet.holdings["MNN"].balance_input("bfx")

print(my_wallet.holdings["MNN"].asset_value())

my_wallet.print_wallet_detail()
