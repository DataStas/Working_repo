from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
cofee_maker.report()

while is_on:
    choice = input(f'what would you like? ({menu.get_items()}) or turn it off?:')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        cofee_maker.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingridients = cofee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingridients and is_payment_successful:
            cofee_maker.make_coffee(drink)