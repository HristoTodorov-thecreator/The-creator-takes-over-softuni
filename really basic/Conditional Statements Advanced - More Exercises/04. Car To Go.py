budget = float(input())
season = input()

car = ''
class_ = ''
price = 0
if budget > 500:
    class_ = 'Luxury class'
    price = budget * 0.90
    car = 'Jeep'
elif 100 < budget <= 500:
    class_ = 'Compact class'
    if season == 'Winter':
        car = 'Jeep'
        price = budget * 0.80
    elif season == 'Summer':
        car = 'Cabrio'
        price = budget * 0.45
elif  budget <= 100:
    class_ = 'Economy class'
    if season == 'Summer':
        price = budget * 0.35
        car = 'Cabrio'
    elif season == 'Winter':
        price = budget  * 0.65
        car = 'Jeep'

print(f'{class_}')
print(f"{car} - {price:.2f}")







