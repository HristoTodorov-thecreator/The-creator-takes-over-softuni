budget = float(input())
season = input()

place = ''
going_to = ''
price = 0
if budget > 3000:
    place = 'Hotel'
    price = budget * 0.90
    if season == 'Summer':
        going_to = 'Alaska'
    elif season == 'Winter':
        going_to = 'Morocco'
elif 1000 < budget <=3000:
    place = 'Hut'
    if season == 'Summer':
        going_to = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        going_to = 'Morocco'
        price = budget * 0.60
if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        going_to = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        going_to = 'Morocco'
        price = budget * 0.45


print(f"{going_to} - {place} - {price:.2f}")



