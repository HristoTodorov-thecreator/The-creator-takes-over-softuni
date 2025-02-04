from math import ceil

number_guests  = int(input())
budget = int(input())

egg_price = 0.45
easter_bread_price = 4.00

easter_bread_for_people =  number_guests / 3 # for each person
ceileaster = ceil(easter_bread_for_people)

eggs_for_the_people = number_guests * 2  # all eggs for the people

price_for_easter_bread_total = ceileaster * easter_bread_price  # total price for easter bread
price_for_eggs_total = eggs_for_the_people * egg_price  # total price for the eggs

total_price = price_for_eggs_total + price_for_easter_bread_total

if budget >= total_price:
    print(f"Lyubo bought {ceileaster} Easter bread and {eggs_for_the_people} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")

