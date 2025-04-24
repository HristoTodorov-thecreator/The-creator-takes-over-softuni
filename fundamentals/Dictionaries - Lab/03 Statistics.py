bakery = {}

total_products = 0
total_quan = 0
while True:
    command = input()
    if command == 'statistics':
        break
    t = command.split(': ')
    key = t[0]
    value = int(t[1])
    total_quan += value

    if key in bakery:
        bakery[key] += value
    else:
        bakery[key] = value
        total_products += 1

print('Products in stock:')
for i,g in bakery.items():
    print(f'- {i}: {g}')

print(f'Total Products: {total_products}\nTotal Quantity: {total_quan}')
