import re

pattern = r'\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])\$'
secondtotal = 0
while True:
    command = input()
    if command == 'end of shift':
        break

    x = re.finditer(pattern,command)
    if x:
        for i in x:
            name = i.group(1)
            item = i.group(2)
            total = float(i.group(3)) * float(i.group(4))
            secondtotal += total
            print(f'{name}: {item} - {total:.2f}')
print(f'Total income: {secondtotal:.2f}')