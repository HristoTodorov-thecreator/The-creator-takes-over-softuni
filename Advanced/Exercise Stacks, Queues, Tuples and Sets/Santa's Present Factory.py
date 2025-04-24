from collections import deque
boxes = [int(x) for x in input().split()]

magic_values = deque([int(x) for x in input().split()])

points = {150:'Doll',250:'Wooden train',300:'Teddy bear',400: 'Bicycle'}
gifts = {}

while boxes and magic_values:

    total = boxes[-1] * magic_values[0]
    if total in points:
        gift = points[total]
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1
        boxes.pop()
        magic_values.popleft()
    elif total < 0:
        boxes.append(boxes.pop() + magic_values.popleft())
    elif total > 0:
        magic_values.popleft()
        boxes[-1] += 15
    else:
        if boxes[-1] == 0:
            boxes.pop()
        if magic_values[0] == 0:
            magic_values.popleft()


if ('Doll' in gifts and 'Wooden train' in gifts) or ('Teddy bear' in gifts and 'Bicycle' in gifts):
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')


if boxes:
    print(f'Materials left: {", ".join(map(str,reversed(boxes)))}')

if magic_values:
    print(f'Magic left: {", ".join(map(str,magic_values))}')

for key,value in sorted(gifts.items()):
    print(f'{key}: {value}')


