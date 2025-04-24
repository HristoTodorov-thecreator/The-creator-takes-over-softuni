from collections import deque

water_left = int(input())

name = input()

waiting_line = deque()

while name != 'Start':
    waiting_line.append(name)
    name = input()


command = input()

while command != 'End':
    if 'refill' in command:

        _,waterr = command.split()
        water_left += int(waterr)





    else:

        thewater = int(command)
        if thewater <= water_left:
            water_left -= thewater
            print(f'{waiting_line.popleft()} got water')
        else:
            print(f'{waiting_line.popleft()} must wait')

    command = input()




print(f'{water_left} liters left')