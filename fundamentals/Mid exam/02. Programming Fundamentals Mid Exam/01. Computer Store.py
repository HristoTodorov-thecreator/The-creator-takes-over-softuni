
taxes = 0
total = 0
total_price_with_tax = 0



while True:

    command = input()
    if command == 'regular':
        total_price_with_tax = total + taxes
        break
    if command == 'special':
        total_price_with_tax = total + taxes
        total_price_with_tax = total_price_with_tax - (total_price_with_tax * 0.10)
        break



    g = float(command)
    if g <= 0:
        print(f'Invalid price!')
        continue

    taxes += (g *0.20)
    total += g

if total_price_with_tax == 0:
    print(f'Invalid order!')
    exit()
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_tax:.2f}$')

