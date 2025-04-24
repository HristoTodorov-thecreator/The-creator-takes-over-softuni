from collections import deque

choc = [int(x) for x in input().split(', ')]
cups_of_milk = [int(x) for x in input().split(', ')]
milkshakes = 0

cups_of_milk = deque(cups_of_milk)

while choc and cups_of_milk:
    if milkshakes == 5:
        break

    last_choc = choc.pop()
    first_cup = cups_of_milk.popleft()
    if last_choc <= 0 and first_cup <= 0:
        continue
    if last_choc <= 0:
        cups_of_milk.appendleft(first_cup)
        continue



    if first_cup <=0:
        choc.append(last_choc)
        continue


    if last_choc == first_cup:

        milkshakes += 1
    else:
        cups_of_milk.append(first_cup)
        last_choc -= 5
        choc.append(last_choc)


if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

if choc:
    print(f'Chocolate: {", ".join(str(x) for x in choc)}')
else:
    print(f'Chocolate: empty')

if cups_of_milk:
    print(f'Milk: {", ".join(str(x) for x in cups_of_milk)}')

else:
    print(f'Milk: empty')