from collections import deque

materials = [int(x) for x in input().split()]

magic_levels = deque([int(x) for x in input().split()])

gifts = {}

def check(total):
    if 100 <= total <= 499:
        if 100 <= total <= 199:
            gift = 'Gemstone'
            if gift not in gifts:
                gifts[gift] = 0
            gifts[gift] += 1

        elif 200 <= total <= 299:
            gift = 'Porcelain Sculpture'
            if gift not in gifts:
                gifts[gift] = 0
            gifts[gift] += 1

        elif 300 <= total <= 399:
            gift = 'Gold'
            if gift not in gifts:
                gifts[gift] = 0
            gifts[gift] += 1

        elif 400 <= total <= 499:
            gift = 'Diamond Jewellery'
            if gift not in gifts:
                gifts[gift] = 0
            gifts[gift] += 1



while materials and magic_levels:
    magic = magic_levels.popleft()
    material = materials.pop()

    total = magic + material

    if 100 <= total <= 499:
        check(total)
    elif total < 100:

        if total % 2 ==0:
            result = (material * 2) + (3 * magic)
            check(result)

        else:
            if total % 2 != 0:
                result = total * 2
                check(result)
    else:
        result = total / 2
        check(result)


if 'Gemstone' in gifts and 'Porcelain Sculpture' in gifts or 'Gold' in gifts and 'Diamond Jewellery' in gifts:
    print(f'The wedding presents are made!')
else:
    print(f'Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join(map(str,materials))}')

if magic_levels:
    print(f'Magic left: {", ".join(map(str,magic_levels))}')


for i,s in sorted(gifts.items()):
    print(f'{i}: {s}')

