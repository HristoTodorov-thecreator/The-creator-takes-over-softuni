import re


pattern = r'([#|])([A-Za-z ]+)\1([0-9]{2})\/([0-9]{2})\/([0-9]{2})\1([0-9]+)\1'


text = input()

x = list(re.finditer(pattern,text))


total = 0



for match in x:




    calories = match.group(6)
    total += int(calories)

all = total // 2000
print(f'You have food to last you for: {all} days!')

for t in x:
    firstitem = t.group(2)
    second_date = t.group(3)
    month = t.group(4)
    year = t.group(5)
    calories = t.group(6)


    print(f'Item: {firstitem}, Best before: {second_date}/{month}/{year}, Nutrition: {calories}')