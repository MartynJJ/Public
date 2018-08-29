
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

class Wallet_bag:
    def __init__(self):
        self.wallets = []
        self.wallet_count = 0
    def add_wallet(self, name="Default", base = " USD"):
        if self.wallet_count > 5:
            print("No more wallets avaliable")
        else:
            self.wallets.append(Wallet(name,base))
            self.wallet_count += 1
            
class Console_interface:
    def __init__(self):
        self.status = False
    def start(self):
        self.status = True
        
        print("Welcome to CrpyCrpyto\nPlease Choose an option:")
        #update to a dictionary with key as description and value as the class function call
        bag = Wallet_bag()
        print("[1] Create New Wallet")
        print("[0] Quit")
        input = int(raw_input())
        if (input == 0):
            quit()
        elif (input == 1):
            name = raw_input("Enter wallet name:\n")
            bag.add_wallet(name)
        
#Start Main:
instance = Console_interface()
instance.start()

        
#Function testings  
'''          
mine = Asset('MNN')
mine.balance_input()
print(mine.total_balance())
mine.balance_input("bmx")
mine.balance_detail()
print(mine.asset_value())

bag = Wallet_bag()
bag.add_wallet()
my_wallet = bag.wallets[0]

my_wallet.add_asset("MNN")
my_wallet.holdings["MNN"].balance_input("bfx")

print(my_wallet.holdings["MNN"].asset_value())

my_wallet.print_wallet_detail()
'''
