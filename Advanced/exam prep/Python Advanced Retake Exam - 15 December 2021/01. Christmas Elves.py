from collections import deque

elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys_made = 0
total_energy_used = 0
turn = 0

while elves and materials:
    elf = elves.popleft()

    if elf < 5:
        continue

    box = materials.pop()
    turn += 1

    needed_energy = box
    made_toys = 1
    gets_cookie = True

    if turn % 3 == 0:
        needed_energy *= 2
        made_toys = 2

    if elf < needed_energy:
        elf *= 2
        elves.append(elf)
        materials.append(box)
        continue

    elf -= needed_energy
    total_energy_used += needed_energy

    if turn % 5 == 0:
        made_toys = 0
        gets_cookie = False

    toys_made += made_toys
    if gets_cookie:
        elf += 1

    elves.append(elf)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy_used}")
if elves:
    print("Elves left:", ', '.join(str(x) for x in elves))
if materials:
    print("Boxes left:", ', '.join(str(x) for x in materials))