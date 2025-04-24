from collections import deque
food_portions = [int(x) for x in input().split(', ')]
staminas = deque([int(x) for x in input().split(', ')])

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])


all_ = []

while food_portions and staminas and peaks:


    last_food = food_portions.pop()
    first_stamina = staminas.popleft()

    total = last_food + first_stamina

    name,diff = peaks[0]

    if total >= diff:
        peaks.popleft()
        all_.append(name)


if not peaks:
    print(f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print(f'Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if all_:
    print(f'Conquered peaks:')
    for name in all_:
        print(name)
