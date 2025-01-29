
airplane_capacity = float(input("Въведете капацитета на багажника: "))
counter = 0
total_volume = 0

while True:
    suitcase = input("Въведете обема на куфара или 'End' за край: ")

    if suitcase == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase_volume = float(suitcase)

    if (counter + 1) % 3 == 0:
        suitcase_volume *= 1.10  # Увеличаваме обема на всеки трети куфар с 10%

    if total_volume + suitcase_volume > airplane_capacity:
        print("No more space!")
        break

    counter += 1
    total_volume += suitcase_volume

print(f'Statistic: {counter} suitcases loaded.')