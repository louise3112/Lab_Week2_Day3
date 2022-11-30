class Customer:
    def __init__(self, input_name, input_wallet, input_age, input_drunkenness):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkenness = input_drunkenness

    def take_money(self, amount):
        self.wallet -= amount

    def increase_drunkenness(self, amount):
        self.drunkenness += amount

    

