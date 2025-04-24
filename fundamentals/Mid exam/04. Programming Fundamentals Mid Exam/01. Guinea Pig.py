quantity_food = float(input()) # for 30 days
quantity_hay = float(input()) # for 30 days
quantity_cover = float(input()) # for 30 days

quantity_food = quantity_food * 1000
quantity_hay = quantity_hay * 1000
quantity_cover = quantity_cover * 1000



not_enough = False

pig_kg = float(input())
pig_grams = pig_kg * 1000

for i in range(1,30 + 1):
    quantity_food -= 300
    if quantity_food <= 0:
        not_enough = True
        break


    if i % 2 == 0:
        needed_hay = quantity_food * 0.05
        quantity_hay -= needed_hay
        if quantity_hay <= 0:
            not_enough = True
            break

    if i % 3 == 0:
        cover_ = pig_grams // 3
        quantity_cover -= cover_

        if quantity_cover <=0:
            not_enough = True
            break


if not_enough:
    print(f"Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, Cover: {quantity_cover / 1000:.2f}.")






