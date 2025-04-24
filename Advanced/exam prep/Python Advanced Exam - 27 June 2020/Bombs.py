from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])

bomb_cas = [int(x) for x in input().split(', ')]


datura_bombs = 0
Cherry_Bombs = 0
Smoke_Decoy_Bombs = 0








while bomb_cas and bomb_effects:
    bomb_effect = bomb_effects.popleft()
    bomb_last = bomb_cas.pop()

    sum_ = bomb_effect + bomb_last

    if sum_ == 40:
        datura_bombs += 1
        if datura_bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3:
            print(f'Bene! You have successfully filled the bomb pouch!')
            break
        continue

    elif sum_ == 60:
        Cherry_Bombs += 1
        if datura_bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3:
            print(f'Bene! You have successfully filled the bomb pouch!')
            break
        continue

    elif sum_ == 120:
        Smoke_Decoy_Bombs += 1
        if datura_bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3:
            print(f'Bene! You have successfully filled the bomb pouch!')
            break
        continue


    bomb_last -= 5
    bomb_cas.append(bomb_last)
    bomb_effects.appendleft(bomb_effect)

if not(datura_bombs >= 3 and Cherry_Bombs >= 3 and Smoke_Decoy_Bombs >= 3):
    print(f"You don't have enough materials to fill the bomb pouch.")


if bomb_effects:
    print(f'Bomb Effects: {", ".join(map(str,bomb_effects))}')
else:
    print(f'Bomb Effects: empty')

if bomb_cas:
    print(f'Bomb Casings: {", ".join(map(str,bomb_cas))}')
else:
    print(f'Bomb Casings: empty')

print(f'Cherry Bombs: {Cherry_Bombs}')
print(f'Datura Bombs: {datura_bombs}')
print(f'Smoke Decoy Bombs: {Smoke_Decoy_Bombs}')









