
size_of_side = float(input())

area = size_of_side * size_of_side * 6


number_of_sheets = int(input())
total = 0


for i in range(1, number_of_sheets + 1):

    length_of_sheet = float(input())
    width_of_sheet = float(input())




    area_of_sheet = length_of_sheet * width_of_sheet



    if i % 5 == 0:
        continue

    elif i % 3 == 0:
        area_of_sheet *= 0.75

    ar = round(area_of_sheet,3)
    total += ar


if area > 0:
    total_covered_percentage = (total / area) * 100
else:
    total_covered_percentage = 0


if total >= area:
    wrap = ((total - area)/ total) * 100
    print("You've covered the gift box!")
    print(f"{wrap:.2f}% wrap paper left.")
else:
    uncovered = (total / area) * 100
    un = 100 - uncovered
    print("You are out of paper!")
    print(f"{un:.2f}% of the box is not covered.")