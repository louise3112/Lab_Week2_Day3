class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def add_money(self, amount):
        self.till += amount

    def buy_drink(self, customer, drink):
        customer.take_money(drink.price)
        self.add_money(drink.price)
