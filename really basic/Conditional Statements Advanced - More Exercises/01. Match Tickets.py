

budget = float(input())
category = input()
number_people_in_group = int(input())
price = 0
if 1 <= number_people_in_group <= 4:
    budget = budget - (budget * 0.75)
elif 5 <= number_people_in_group <=9:
    budget = budget - (budget * 0.60)
elif 10 <= number_people_in_group <=24:
    budget = budget - (budget * 0.50)
elif 25 <= number_people_in_group <=49:
    budget = budget - (budget * 0.40)
elif number_people_in_group >= 50:
    budget = budget - (budget * 0.25)

if category == 'VIP':
    price = 499.99
elif category == 'Normal':
    price = 249.99

total_for_tickets = price * number_people_in_group


if budget >= total_for_tickets:
    print(f"Yes! You have {budget - total_for_tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_for_tickets - budget:.2f} leva.")
