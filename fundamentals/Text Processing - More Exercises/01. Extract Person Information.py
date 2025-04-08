import re

first_pattern = r'@([A-Za-z]+)\||#([0-9]+)\*'
number = int(input())





for i in range(number):
    info = input()
    x = re.finditer(first_pattern, info)

    age = ''
    name = ''
    counter = 0
    for match in x:
        if match.group(1):
            name = match.group(1)
        if match.group(2):
            age = match.group(2)

    print(f'{name} is {age} years old.')





