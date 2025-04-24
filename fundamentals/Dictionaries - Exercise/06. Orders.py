commands = input().split(' ')


product_quan = {}
product_prices = {}

while 'buy' not in commands:
    product = commands[0]
    price = float(commands[1])
    quantity = int(commands[2])

    if product not in product_quan.keys():
        product_quan[product] = 0
        product_prices[product] = 0.00

    product_quan[product] += quantity
    product_prices[product] = price
    commands = input().split(' ')
    if "buy" in commands:
        break

for key, value in product_quan.items():
    price = value * product_prices[key]
    print(f"{key} -> {price:.2f}")