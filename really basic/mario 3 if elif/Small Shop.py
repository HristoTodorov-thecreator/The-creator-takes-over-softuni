
product = input()
city = input()
amount = float(input())

total = 0

if city == 'Sofia':
    if product == "coffee":
        total = amount * 0.50
        print(total)
    elif product == 'water':
        total = amount * 0.80
        print(total)
    elif product == 'beer':
        total = amount * 1.20
        print(total)
    elif product == 'sweets':
        total = amount * 1.45
        print(total)
    elif product == 'peanuts':
        total = amount * 1.60
        print(total)

elif city == 'Plovdiv':
    if product == "coffee":
        total = amount * 0.40
        print(total)
    elif product == 'water':
        total = amount * 0.70
        print(total)
    elif product == 'beer':
        total = amount * 1.15
        print(total)
    elif product == 'sweets':
        total = amount * 1.30
        print(total)
    elif product == 'peanuts':
        total = amount * 1.50
        print(total)


elif city == 'Varna':
    if product == "coffee":
        total = amount * 0.45
        print(total)
    elif product == 'water':
        total = amount * 0.70
        print(total)
    elif product == 'beer':
        total = amount * 1.10
        print(total)
    elif product == 'sweets':
        total = amount * 1.35
        print(total)
    elif product == 'peanuts':
        total = amount * 1.55
        print(total)
