# Map of Menu
'''
No. Toppings        small   regular large
1.  Margherita      63.750  85.000  106.250
2.  Pepperoni       71.250  95.000  118.750
3.  Meat Lovers     67.500  90.000  112.500
4.  Super Supreme   71.250  95.000  118.750
5.  Cheeseburger    67.500  90.000  112.500
6.  Double Cheese   63.500  86.000  107.500

Additional
Extra Meat of Choice    +13.000
Extra Cheese            +13.000
Extra Basil             +6.000

Crust Price
Thin Crust              +4.000
Thick Crust             +7.000
Pan Crust               +4.000
Cheese Burst Crust      +13.000
Stuffed Crust           +10.000
'''

# Pizza menu
pizza_menu = {
    '1': {'name': 'Margherita', 'small' : 63.750, 'regular': 85.000, 'large': 106.250},
    '2': {'name': 'Pepperoni', 'small' : 71.250, 'regular': 95.000, 'large': 118.750},
    '3': {'name': 'Meat Lovers', 'small' : 67.500, 'regular': 90.000, 'large': 112.500},
    '4': {'name': 'Super Supreme', 'small' : 71.250, 'regular': 95.000, 'large': 118.750},
    '5': {'name': 'Cheeseburger', 'small' : 67.500, 'regular': 90.000, 'large': 112.500},
    '6': {'name': 'Double Cheese', 'small' : 63.500, 'regular': 86.000, 'large': 107.500}
}

# Pizza size
# price calculated in percentage
pizza_size = {
    '1': {'name': 'Small', 'price': -25},
    '2': {'name': 'Regular', 'price': 0},
    '3': {'name': 'Large', 'price': 25}
}

# Pizza topping
pizza_topping = {
    '1': {'name': 'None', 'price': 0},
    '2': {'name': 'Extra Meat of Choice', 'price': 13},
    '3': {'name': 'Extra Cheese', 'price': 13},
    '4': {'name': 'Extra Basil', 'price': 6}
}

# Pizza crust
pizza_crust = {
    '1': {'name': 'Normal Crust', 'price': 0},
    '2': {'name': 'Thin Crust', 'price': 4},
    '3': {'name': 'Thick Crust', 'price': 7},
    '4': {'name': 'Pan Crust', 'price': 4},
    '5': {'name': 'Cheese Burst Crust', 'price': 13},
    '6': {'name': 'Stuffed Crust', 'price': 10}
}

def range_input(msg, first, end):
    """
        Prompt the user to input an integer within a specified range and ensure the user provides a valid input.
    """
    while True:
        try:
            value = int(input(msg))
            if value < first or value > end:
                raise ValueError
            return str(value)
        except ValueError:
            print(f"Please input number between {first} and {end}")

def print_menu():
    """
        Show the pizza menu.
    """
    print("Pizza Menu")
    for key, value in pizza_menu.items():
        print(f"{key}. {value['name']}")
    print()

def print_size():
    """
        Show the pizza size. 
    """
    print("Pizza Size")
    for key, value in pizza_size.items():
        print(f"{key}. {value['name']}: {value['price']}%")
    print()

def print_topping():
    """
        Show the pizza topping.
    """
    print("Pizza Topping")
    for key, value in pizza_topping.items():
        print(f"{key}. {value['name']}: {value['price']}k")
    print()

def print_crust():
    """
        Show the pizza crust.
    """
    print("Pizza Crust")
    for key, value in pizza_crust.items():
        print(f"{key}. {value['name']}: {value['price']}k")
    print()

if __name__ == "__main__":
    # Show the menu
    print_menu()
    pizza = range_input("Choose your pizza: ", 1, len(pizza_menu))
    print_size()
    size = range_input("Choose your size: ", 1, len(pizza_size))
    print_topping()
    topping = range_input("Choose your topping: ", 1, len(pizza_topping))
    print_crust()
    crust = range_input("Choose your crust: ", 1, len(pizza_crust))

    # Calculate the price    
    pizza_price = pizza_menu[pizza][pizza_size[size]['name'].lower()]
    pizza_price += pizza_topping[topping]['price']
    pizza_price += pizza_crust[crust]['price']
    
    # Show the total price
    print(f"Total price: {format(pizza_price, '.3f')}")
    