number_dancers = int(input())
points = float(input())
season = input() # winter or summer
place = input()  # Bulgaria or Abroad

price_won = number_dancers * points

if place == 'Abroad':
    price_won = price_won + (price_won * 0.50)

if season == 'summer':
    if place == 'Bulgaria':
        price_won = price_won -(price_won * 0.05)
    elif place == 'Abroad':
        price_won = price_won - (price_won * 0.10)
elif season == 'winter':
    if place == 'Bulgaria':
        price_won = price_won - (price_won * 0.08)
    elif place == 'Abroad':
        price_won = price_won - (price_won * 0.15)


charitypercent = price_won * 0.75
price_won = price_won - charitypercent  # people give the money for good

for_one_dancer = price_won / number_dancers

print(f'Charity - {charitypercent:.2f}')
print(f'Money per dancer - {for_one_dancer:.2f}')
