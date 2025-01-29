buyed_food = int(input())
total_in_grams = buyed_food * 1000
total_eated = 0
while True:
    eated_by_the_dog = input()
    if eated_by_the_dog == 'Adopted':
        break
    g = int(eated_by_the_dog)
    total_eated += g

if total_in_grams >= total_eated:
    print(f"Food is enough! Leftovers: {total_in_grams - total_eated} grams." )
else:
    print(f"Food is not enough. You need {total_eated - total_in_grams} grams more." )
