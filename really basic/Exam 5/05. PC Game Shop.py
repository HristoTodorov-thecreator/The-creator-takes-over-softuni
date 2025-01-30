n = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for i in range(n):
    name_game = input()

    if name_game == 'Hearthstone':
        Hearthstone += 1

    elif name_game == 'Fornite':
        Fornite += 1

    elif name_game == 'Overwatch':
        Overwatch += 1

    else:
        Others += 1

print(f'Hearthstone - {(Hearthstone / n) * 100:.2f}%')
print(f'Fornite - {(Fornite / n) * 100:.2f}%')
print(f'Overwatch - {(Overwatch / n) * 100:.2f}%')
print(f'Others - {(Others / n) * 100:.2f}%')



