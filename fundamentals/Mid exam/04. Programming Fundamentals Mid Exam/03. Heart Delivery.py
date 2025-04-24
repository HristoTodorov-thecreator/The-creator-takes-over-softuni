neigbours = [int(g) for g in input().split('@')]

startindex = 0

position = 0

while True:


    command = input()
    if command == 'Love!':
        break

    command = command.split(' ')
    action,index_ = command[0],int(command[1])

    if action == 'Jump':
        position += index_
        if position < len(neigbours):
            if neigbours[position] > 0:
                neigbours[position] -=2
                if neigbours[position] <=0:
                    print(f"Place {position} has Valentine's day." )
            else:
                print(f"Place {position} already had Valentine's day.")
        else:
            position = 0
            if neigbours[startindex] > 0:
                neigbours[startindex] -= 2
                if neigbours[startindex] <= 0:
                    print(f"Place {position} has Valentine's day.")
            else:
                print(f"Place {position} already had Valentine's day.")

print(f"Cupid's last position was {position}.")
if sum(neigbours) == 0:
    print(f"Mission was successful.")

else:
    counter = 0
    for i in neigbours:

        if i !=0:
            counter += 1

    print(f'Cupid has failed {counter} places.')










