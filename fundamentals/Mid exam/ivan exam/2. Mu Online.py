initial_health = 100
bitcoins_start = 0

rooms = input().split('|')

best_room = 0

dead = False

for i in rooms:
    best_room += 1
    action,hp = i.split()



    if action == 'potion':
        t_health = initial_health
        initial_health += int(hp)
        if initial_health > 100:
            initial_health = 100
        real = initial_health - t_health
        print(f'You healed for {real} hp.')
        print(f'Current health: {initial_health} hp.')
    elif action == 'chest':

        bitcoins_start += int(hp)
        print(f'You found {hp} bitcoins.')
    else:
        initial_health -= int(hp)
        if initial_health > 0:
            print(f'You slayed {action}.')
        else:
            print(f'You died! Killed by {action}.')
            print(f'Best room: {best_room}')
            dead = True
            break
if not dead:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins_start}')
    print(f'Health: {initial_health}')

