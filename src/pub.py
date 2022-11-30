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
            customer.change_drunkenness(drink.alchol_level)

    def sell_food(self, customer, food):
        customer.take_money(food.price)
        self.add_money(food.price)
        customer.change_drunkenness(food.rejuvenation_level)
            
