from collections import deque
cups = deque([int(x) for x in input().split()])

bottles = [int(s) for s in input().split()]

allwater = 0


while cups and bottles:
    bottle = bottles.pop()
    cup = cups.popleft()

    if bottle >= cup:
        water = bottle - cup
        allwater += water
    else:
        cups.appendleft(cup - bottle)


if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {allwater}")
