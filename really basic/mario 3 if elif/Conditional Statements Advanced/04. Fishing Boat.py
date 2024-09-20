Budget = int(input())
Season = input()
fisherman = int(input())

total = 0

if Season == 'Spring':
    total = 3000
elif Season == 'Autumn' or Season == 'Summer':
    total = 4200
elif Season == 'Winter':
    total = 2600

if fisherman <= 6:
    total = total - (total * 0.10)
elif 7 <= fisherman <= 11:
    total = total - (total * 0.15)
elif fisherman >= 12:
    total = total - (total * 0.25)

if Season != 'Autumn' and fisherman % 2 == 0:
    total = total - (total * 0.05)

if Budget >= total:
    print(f"Yes! You have {Budget - total:.2f} leva left.")

elif Budget < total:
    print(f"Not enough money! You need {total - Budget:.2f} leva.")
