capacity = int(input())
fans = int(input())


fans_in_a = 0
fans_in_b = 0
fans_in_v = 0
fans_in_g = 0



for i in range (fans):
    g = input()
    if g == 'A':
        fans_in_a += 1


    if g == 'B':
        fans_in_b += 1


    if g == 'V':
        fans_in_v += 1


    if g == 'G':
        fans_in_g += 1

print(f'{fans_in_a / fans * 100:.2f}%')
print(f'{fans_in_b / fans * 100:.2f}%')
print(f'{fans_in_v / fans * 100:.2f}%')
print(f'{fans_in_g / fans * 100:.2f}%')
print(f'{fans / capacity * 100:.2f}%')
