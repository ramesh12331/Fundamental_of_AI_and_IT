def display_menu(menu):
    print('Menu')
    print('-' * 25)
    for item, price in menu.items():
        print(f'{item}: {price}')


def take_order(menu):
    order = {}
    item = input("Enter the item (or 'done' to finish): ")
    while item != 'done':
        if item in menu:
            quantity = int(input(f"Quantity for {item}: "))
            order[item] = order.get(item, 0) + quantity
        else:
            print('Item is not available in menu')

        item = input("Enter the item (or 'done' to finish): ")
    return order


def calculate_bill(menu, order):
    total_amount = 0
    for item, quantity in order.items():
        item_cost = menu[item] * quantity
        total_amount += item_cost

    discount = total_amount * 0.1 if total_amount > 1000 else 0

    return total_amount, discount


def print_bill(menu, order, total_amount, discount):
    print('Bill\n')
    print('-' * 20)
    for item, quantity in order.items():
        print(f"{item} x {quantity} = {menu[item] * quantity}")

    if discount:
        print(f'Discount applied: {discount}')

    print(f'Total amount: {total_amount - discount}')


menu = {
    'Four Cheese Pizza'   : 400,
    'BBQ Bacon Burger'    : 319,
    'Lasagna'             : 340,
    'Onion Rings'         : 140,
    'Minestrone Soup'     : 145,
    'Caesar Salad'        : 199,
    'Coca Cola'           : 60,
    'Fresh Lime Soda'     : 80,
    'Mango Lassi'         : 120,
    'Chocolate Brownie'   : 180,
    'Cheesecake'          : 220,
}

display_menu(menu)

order = take_order(menu)

print(order)

total_amount, discount = calculate_bill(menu, order)

print_bill(menu, order, total_amount, discount)