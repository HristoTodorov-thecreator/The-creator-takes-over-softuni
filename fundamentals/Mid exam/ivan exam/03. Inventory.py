status = list(map(int,input().split('>')))

status_for_warship = list(map(int,input().split('>')))

maximum_health = int(input())
gone = False
while True:
    command = input().split()
    if command[0] == 'Retire':
        break
    if command[0] == 'Fire':
        index = int(command[1])
        action = int(command[2])
        if index in range(len(status_for_warship)):
            status_for_warship[index] -= action
            if status_for_warship[index] <= 0:
                gone = True
                print("You won! The enemy ship has sunken.")
                break
        else:
            continue

    elif command[0] == 'Defend':
        index = int(command[1])
        indextwo = int(command[2])

        action = int(command[3])
        if index in range(len(status)):
           if indextwo in range(len(status)):
               for n in range(index,indextwo + 1):
                   status[n] -= action
                   if status[n] <= 0:
                       gone = True
                       print(f'You lost! The pirate ship has sunken.')
                       break
               if gone:
                   break
           else:
               continue
        else:
            continue

    elif command[0] == 'Repair':
        index = int(command[1])
        action = int(command[2])
        if index in range(len(status)):
            status[index] += action
            if status[index] > maximum_health:
                status[index] = maximum_health

        else:
            continue


    elif command[0] == 'Status':
        count = 0
        for index in range(len(status)):
            if status[index] < maximum_health / 5:
                count += 1
        print(f'{count} sections need repair.')


if not gone:
    print(f'Pirate ship status: {sum(status)}')
    print(f"Warship status: {sum(status_for_warship)}")