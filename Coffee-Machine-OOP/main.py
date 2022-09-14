import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_Machine = CoffeeMaker()
paying_process = MoneyMachine()
menu = Menu()
options = menu.get_items()


machine_on = True
while machine_on:
    answer = input(f"What would you like {options} : ").lower()
    if answer == "off"
        machine_on = False
    elif answer == "report":
        coffee_Machine.report()
        paying_process.report()
    else:
        drink = menu.find_drink(answer)
        if type(drink) == MenuItem:
            if coffee_Machine.is_resource_sufficient(drink):
                if paying_process.make_payment(drink.cost):
                    coffee_Machine.make_coffee(drink)




