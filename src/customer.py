class Customer:
    def __init__(self, input_name, input_wallet, input_age, input_drunkenness):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkenness = input_drunkenness

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def change_drunkenness(self, amount):
        self.drunkenness += amount
        if self.drunkenness < 0:
            self.drunkenness = 0

    

