wanted_year = 1800
years_old = 18

money_he_get = float(input())
year_wanted_to_live = int(input())

for_ = year_wanted_to_live - wanted_year

total = 0
total += money_he_get
for i in range(for_ + 1):
    if i % 2 == 0:
        total -= 12000
    else:
        total -= 12000 + 50 * years_old
    years_old += 1


if total < 0:
    print(f"He will need {abs(total):.2f} dollars to survive." )


elif money_he_get >= total:
    print(f"Yes! He will live a carefree life and will have {abs(total):.2f} dollars left." )



