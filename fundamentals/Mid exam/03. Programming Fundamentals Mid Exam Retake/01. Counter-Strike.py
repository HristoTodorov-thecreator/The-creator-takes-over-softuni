




energy = int(input())

won_battles = 0
command = input()
while command  != 'End of battle':

    number = int(command)
    energy -= number



    if energy <0:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {energy + number} energy')

        break
    won_battles += 1
    if won_battles % 3 ==0:
        energy += won_battles

    command = input()


else:
    print(f"Won battles: {won_battles}. Energy left: {energy}" )



