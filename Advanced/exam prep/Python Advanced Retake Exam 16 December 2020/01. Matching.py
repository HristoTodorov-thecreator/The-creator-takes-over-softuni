from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches = 0
while males and females:

    if females[0] <= 0:
        del females[0]
        continue
    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    if males[-1] <= 0:
        del males[-1]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue

    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
        continue
    else:
        males.append(male - 2)

print(f'Matches: {matches}')

if males:
    males = reversed(males)
    print(f'Males left: {", ".join(map(str,males))}')

else:
    print(f'Males left: none')

if females:
    print(f'Females left: {", ".join(map(str,females))}')

else:
    print(f'Females left: none')






