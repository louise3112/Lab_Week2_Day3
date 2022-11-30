class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

        self.stock = 0.00
        for drink in self.drinks:
            self.stock += self.drinks[drink]

    def add_money(self, amount):
        self.till += amount

    def reduce_drinks_stock(self, drink_name):
        self.drinks[drink_name] -= 1

    def sell_drink(self, customer, drink):
        if customer.age >= 18 and customer.drunkenness < 10:
            customer.take_money(drink.price)
            self.add_money(drink.price)
            self.reduce_drinks_stock(drink.name)
            customer.change_drunkenness(drink.alchol_level)

    def sell_food(self, customer, food):
        customer.take_money(food.price)
        self.add_money(food.price)
        customer.change_drunkenness(food.rejuvenation_level)
    
    def stock_value(self, list_of_available_drinks):
        total_stock_value = 0
        for drink in list_of_available_drinks: #drink = instance of drink
            total_drink_value = drink.price * self.drinks[drink.name]
            total_stock_value += total_drink_value
        
        return total_stock_value
