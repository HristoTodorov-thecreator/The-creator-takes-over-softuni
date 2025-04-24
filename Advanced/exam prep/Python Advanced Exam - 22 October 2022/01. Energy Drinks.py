
from collections import deque
seq_mil_caf = [int(x) for x in input().split(', ')]
seq_ener_drinks = deque([int(x) for x in input().split(', ')])


max_mil = 300
start_mil = 0

while seq_ener_drinks and seq_mil_caf:
    last_mil_caf = seq_mil_caf.pop()
    first_ener_drink = seq_ener_drinks.popleft()

    result = last_mil_caf * first_ener_drink

    if start_mil + result <= max_mil:
        start_mil += result

    else:
        seq_ener_drinks.append(first_ener_drink)
        if start_mil - 30 < 0:
            continue
        else:
            start_mil -= 30

if not seq_ener_drinks:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
if seq_ener_drinks:
    print(f'Drinks left: {", ".join(map(str,seq_ener_drinks))}')

print(f'Stamat is going to sleep with {start_mil} mg caffeine.')