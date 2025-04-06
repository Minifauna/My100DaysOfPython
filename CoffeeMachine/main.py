from data import MENU
from data import resources
power_state = True

def report():
    """When the user enters 'report' to the prompt, print current resource values"""
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffee: {resources['coffee']}g')

def recipe_selection(coffee_type):
    """takes coffee selection input, provides dictionary of ingredients out"""
    recipe_requirements = MENU[coffee_type]['ingredients']
    return recipe_requirements

def wwyl():
    """Request user input, could be coffee or off or report"""
    user_request = str(input('What would you like? (espresso/latte/cappuccino): ').lower())
    return user_request

def resource_check(recipe_to_check, current_resources):
    """check recipe requirements against current resources, return updated resources"""
    for keys in recipe_to_check:
        enough = True
        if current_resources[keys] < recipe_to_check[keys]:
            print(f'Sorry there is not enough {keys}.')
            enough = False
            return enough
        else:
            for x, y in recipe_to_check.items():
                current_resources[x] -= recipe_to_check[x]
            return current_resources

def payment(coffee_type):
    price = (MENU[coffee_type]['cost']) * 100
    print(f'Cost: {("{:.2f}".format(price/100))}')
    print('Please insert one type of coin at a time.\n')
    quarters = int(input('# of quarters: '))
    dimes = int(input('# of dimes: '))
    nickels = int(input('# of nickels: '))
    pennies = int(input('# of pennies: '))
    money_taken = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
    difference = (price - money_taken) / 100
    return difference

def tender_check(coffee_type):
    difference = payment(coffee_type)
    paid = False
    while not paid:
        if difference == 0:
            paid = True
            return paid
        elif difference > 0:
            print('Insufficient total, coins refunded.\nPlease try again.')
            difference = payment(coffee_type)
        elif difference < 0:
            paid = True
            print(f'Your change is {("{:.2f}".format(difference))}.')
            return paid


def coffee_machine(resource_source):
    power = True
    user_request = wwyl()
    if user_request == 'report':
        report()
    elif user_request == 'off':
        power = False
        return power
    else:
        enough_remaining = resource_check(recipe_selection(user_request), resources)
        if not enough_remaining:
            user_request = wwyl()
            return user_request
        else:
            has_paid = tender_check(user_request)
            if has_paid:
                resource = resource_check(recipe_selection(user_request), resource_source)
                print(f'Here is your {user_request}\nHave a nice day!')
                coffee_machine(resource)
            else:
                coffee_machine(resource_source)
    return power

while power_state:
    power_state = coffee_machine(resources)

