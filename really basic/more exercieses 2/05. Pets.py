from math import ceil
from math import floor


num_days = int(input())
left_food = int(input())
food_for_doog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

food_for_turtle = food_for_turtle / 1000

fooddogtot = food_for_doog * num_days
foodcattot = food_for_cat * num_days
foodturtot = food_for_turtle * num_days

total = foodturtot + fooddogtot + foodcattot

if left_food >= total:
    print(f"{floor(left_food - total)} kilos of food left.")
else:
    print(f'{ceil(total - left_food)} more kilos of food are needed.')