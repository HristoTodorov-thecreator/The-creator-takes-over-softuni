season = input()
km_a_month = float(input())

price = 0


if 10000 < km_a_month <= 20000:
    price = 1.45

elif 5000 < km_a_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.95
    elif season == 'Summer':
        price = 1.10
    elif season == 'Winter':
        price = 1.25


elif km_a_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.75
    elif season == 'Summer':
        price = 0.90
    elif season == 'Winter':
        price = 1.05  # money for km

total = (km_a_month * price)  # for one month
total4 = total * 4
tax = total4 * 0.10
total4withtax = total4 - tax

print(f'{total4withtax:.2f}')


