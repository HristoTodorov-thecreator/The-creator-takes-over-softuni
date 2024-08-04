bottles = int(input())

total = bottles * 750  # one bottle = 750 ml
m =0
counter = 0
pot = 0
plate = 0
while True:
    g = input()
    if g == 'End':
        break
    m = int(g)
    counter += 1
    if counter % 3 == 0:
        total -= m * 15
        pot += m
    else:
        total -= m * 5
        plate += m



    if total < 0:
        break

if total >= 0:
    print(f'Detergent was enough!')
    print(f"{plate} dishes and {pot} pots were washed.")
    print(f"Leftover detergent {abs(total)} ml.")
else:
    print(f"Not enough detergent, {abs(total)} ml. more necessary!")
