
class Asset:
    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_list = {
            "bfx" : 0,
            "gdax" : 0,
            "blockchain_info" : 0
            }
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
        #INSERT CMC API call here
        price = 0.05 #temp price
        return (price)
    def asset_value(self, base = "USD"):
        return (self.total_balance() * self.asset_price(base))

class API_Caller:
    def __init__(self, url):
        self.url = url
        
        
#Function testings            
mine = Asset('MNN')
mine.balance_input()
print(mine.total_balance())
mine.balance_input("bmx")
mine.balance_detail()
print(mine.asset_value())
