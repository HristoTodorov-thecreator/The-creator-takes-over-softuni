import re

command = input()

total = 0
items = []
while command != 'Purchase':


    pattern = r'>>([A-Za-z]+)<<([0-9\.]+)\!([0-9]+)\b'

    x = re.search(pattern,command)

    if x:
        item,cost,digit = x.groups()
        items.append(item)
        total += float(cost) * int(digit)
    command = input()

print(f'Bought furniture:')

for n in items:
    print(n)


print(f'Total money spend: {total:.2f}')
