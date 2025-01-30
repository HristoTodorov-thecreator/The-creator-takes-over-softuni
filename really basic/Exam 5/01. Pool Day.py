from math import ceil

number_people = int(input())
price = float(input())
price_for_one_sun_lounger = float(input())
price_for_one_umbrella = float(input())

total_tax = number_people * price
for_sun_lounger = number_people * 0.75
pr = ceil(for_sun_lounger)
price_for_sun_lounger = pr * price_for_one_sun_lounger

total_umbrellas = number_people / 2
gr = ceil(total_umbrellas)
total_price_for_umbrellas = gr * price_for_one_umbrella

total_price  = total_tax + total_price_for_umbrellas + price_for_sun_lounger
print(f'{total_price:.2f} lv.')
