from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffemaker = CoffeeMaker()
moneymachine = MoneyMachine()

isOn = True
while isOn:
    ordername = input(f"What would you like ?({menu.get_items()})=")
    if ordername == 'off':
        isOn = False
    elif ordername == 'report':
        coffemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(ordername)
        if coffemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffemaker.make_coffee(drink)

