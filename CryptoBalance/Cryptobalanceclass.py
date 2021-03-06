import os
class Asset:
    def __init__(self, symbol):
        self.symbol = symbol
        self.status = False
        self.balance_list = {}
        self.API = API_Caller("url here")
        self.actions = [Console_action_index(0, "[0] Back to wallet", self.close),
                        Console_action_index(1, "[1] Balance Detail", self.balance_detail),
                        Console_action_index(2, "[2] Balance Input", self.balance_input)]
                        #Console_action_index(3, "[3] , )
    def start(self):
        self.status = True
        self.balance_detail()
        while (self.status == True):
            for i in range(len(self.actions)):
                print(self.actions[i].give_desc())
            action = int(raw_input("Enter action: "))
            self.actions[action].action()
            print("\n\n\n\n\n")
    def close(self):
        self.status = False
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
        self.status = False
        self.actions = [Console_action_index(0, "[0] Close Wallet", self.close_wallet),
                        Console_action_index(1, "[1] Add asset", self.add_asset),
                        Console_action_index(2, "[2] Show Wallet Value", self.wallet_value),
                        Console_action_index(3, "[3] Print wallet detail", self.print_wallet_detail),
                        Console_action_index(4, "[4] View asset detail", self.open_asset)]
                        #action to dive into asset break down - trigger to asset UI
                        
                        
    def open_wallet(self): # Interface function - Fill in next steps of wallet interface
        self.status = True
        self.print_wallet_detail()
        while (self.status == True):
            for i in range(len(self.actions)):
                print(self.actions[i].give_desc())
            action = int(raw_input("Enter action: "))
            self.actions[action].action()
            print("\n\n\n\n\n")
    def open_asset(self):
        self.print_wallet_detail()
        asset = raw_input("Enter symbol to view:\n")
        self.holdings[asset].start()
    def close_wallet(self):
        self.status = False
    def give_name(self):
        return str(self.name)
    def add_asset(self, symbol=None):
        if (symbol == None):
            symbol = raw_input("Enter Symbol: ")
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
            print("No more wallets avaliable\n\n\n")
        else:
            self.wallets.append(Wallet(name,base))
            self.wallet_count += 1

class File_manager:
    def __init__(self):
        self.files = []
        self.extension = "cbf"
        self.dir = "./save/"
        self.current_file = 0
    def dir_scan(self):
        for files in range(len(os.listdir(self.dir))):
            self.files.append((os.listdir(self.dir))[files])
    def dir_show(self):
        self.dir_scan()
        for i in range(len(self.files)):
            print("[%d] %s" % (i, self.files[i]))
    def file(self):
        file == None
        file = raw_input("Select file number")
        if (file == None):
            return self.files[self.current_file]
        else:
            self.current_file = file
            return self.files[self.current_file]
class Console_interface:
    def __init__(self):
        self.status = False
        self.bag = Wallet_bag()
        self.files = File_manager()
        self.actions = [Console_action_index(0, "[0] Quit", self.quit_prog),
                        Console_action_index(1, "[1] Create new wallet", self.new_wallet),
                        Console_action_index(2, "[2] Open wallet", self.open_wallet),
                        Console_action_index(3, "[3] Dir Show", self.files.dir_show),
                        Console_action_index(4, "[4] Confirm/Change File", self.files.file)
                        ]
                        
    def quit_prog(self):
        self.status = False
    def new_wallet(self):
        name = raw_input("Enter wallet name:\n")
        self.bag.add_wallet(name)
    def open_wallet(self):
        if (self.bag.wallet_count == 0):
            print("\n\n\nNo wallets avaliable, please create a wallet.\nEnter to continue")
            raw_input()
        else:
            print("\n\n\n")
            for i in range(len(self.bag.wallets)):
                print("[%d] : %s" % (int(i), self.bag.wallets[i].give_name()))
            wallet_choice = int(raw_input("Select wallet to open:\n"))
            self.bag.wallets[wallet_choice].open_wallet()
    def start(self): # Interface function
        self.status = True
        while(self.status == True):
            print("\n\n\n\nWelcome to CrpyCrpyto\nPlease Choose an option:")
            for i in range(len(self.actions)):
                print(self.actions[i].give_desc())
            action =(raw_input("Enter action: "))
            selection = action_choice(action)
            selection.validate()
            if (selection.report()):
                self.actions[selection.give_choice()].action()
            if(selection.give_choice() != 0):
                raw_input()
class action_choice:
    def __init__(self, choice, validation=None):
        self.choice = choice
        self.validation = validation
        self.status = False
    def validate(self):
        try:
            self.choice = int(self.choice)
        except ValueError:
            self.status = False
        if (type(self.choice) != int):
            self.status = False
            print("Choice entered is not valid")
        else:
            self.status = True
    def report(self):
        return self.status
    def give_choice(self):
        return self.choice
class Console_action_index:
    def __init__(self, index, desc, action):
        self.index = index
        self.desc = desc
        self.action = action
    def give_desc(self):
        return self.desc

        
        
#int Main():


        
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
