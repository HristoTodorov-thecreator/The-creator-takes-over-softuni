Flower_type = input()
number_flowers = int(input())
budget = int(input())

total = 0
if Flower_type == 'Roses':
    if number_flowers > 80:
        total = (number_flowers * 5) - (number_flowers * 5) * 0.10  # total price if the count is > 90 DISCOUNT 10%
    else:
        total = (number_flowers * 5)  # total price

elif Flower_type == 'Dahlias':
    if number_flowers > 90:
        total = (number_flowers * 3.80) - (number_flowers * 3.80) * 0.15 # total price if the count is > 90 DISCOUNT 15%
    else:
        total = (number_flowers * 3.80)  # total price

elif Flower_type == 'Tulips':
    if number_flowers > 80:
        total = (number_flowers * 2.80) - (number_flowers * 2.80) * 0.15  # total price if the count is >80 DISCOUNT 15%
    else:
        total = (number_flowers * 2.80)  # total price

elif Flower_type == 'Narcissus':
    if number_flowers < 120:
        total = (number_flowers * 3) + (number_flowers * 3) * 0.15  # total price if the count is < 120 ADD 15%
    else:
        total = (number_flowers * 3)  # total price

elif Flower_type == 'Gladiolus':
    if number_flowers < 80:
        total = (number_flowers * 2.50) + (number_flowers * 2.50) * 0.20  # total price if the count is < 80  ADD 20%
    else:
        total = (number_flowers * 2.50)  # total price

if budget >= total:
    print(f"Hey, you have a great garden with {number_flowers} {Flower_type} and {budget - total:.2f} leva left.")
elif budget < total:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
