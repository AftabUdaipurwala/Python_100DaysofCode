from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 : PRINT REPORT
money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# TODO 2 : CHECK IF RESOURCES ARE SUFFICIENT
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ? {options} : ")
    # TODO 3 : CHECK FOR USER INPUT
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 4 : CHECK RESOURCES AND TRANSACTIONS
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            # TODO 5 : MAKE COFFEE
            coffee_maker.make_coffee(drink)
