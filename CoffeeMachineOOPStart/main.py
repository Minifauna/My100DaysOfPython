from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
USD = '{0:.2f}'
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
user_input = str(input(f'Please select a drink\n{menu.get_items()[:-1]}\n')).lower()
drink_selection = menu.find_drink(user_input)
def making_coffee(drink_choice):
    if drink_choice:
        if coffee_maker.is_resource_sufficient(drink_choice):
            print(f'Your {drink_choice.name} costs ${USD.format(drink_choice.cost)}')
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)
                user_inputs = str(input(f'Please select a drink\n{menu.get_items()[:-1]}\n')).lower()
                drink_selections = menu.find_drink(user_inputs)
                return drink_selections
    coffee_maker.report()
    money_machine.report()
    user_inputs = str(input(f'Please select a drink\n{menu.get_items()[:-1]}\n')).lower()
    drink_selections = menu.find_drink(user_inputs)
    return drink_selections

while coffee_maker:
    if user_input == 'off':
        print('Powering down.')
        break
    drink_selection = making_coffee(drink_selection)
