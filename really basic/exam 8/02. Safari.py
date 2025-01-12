

budget = float(input())
liters_fuel = float(input())
day_of_the_week = input()

price_for_liter_fuel = 2.10
tour_guide = 100

total_fuel = liters_fuel * price_for_liter_fuel
total_price = tour_guide + total_fuel

if day_of_the_week == 'Saturday':
    total_price = total_price - (total_price * 0.10)

elif day_of_the_week == 'Sunday':
    total_price = total_price - (total_price * 0.20)

if budget >= total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")


