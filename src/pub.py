class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def add_money(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness < 10:
            customer.take_money(drink.price)
            self.add_money(drink.price)
            # customer.drunkenness += drink.alchol_level
            customer.increase_drunkenness(drink.alchol_level)
            
