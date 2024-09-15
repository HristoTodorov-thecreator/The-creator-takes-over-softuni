number_km = int(input())
day_or_night = input()
price = 0
if number_km < 20:
    if day_or_night == 'day':
        price = 0.70 + number_km * 0.79
    elif day_or_night == 'night':
        price = 0.70 + number_km * 0.90
elif 20 <= number_km < 100 :
    price = number_km * 0.09
elif number_km >= 100:
    price = number_km * 0.06

print(f'{price:.2f}')