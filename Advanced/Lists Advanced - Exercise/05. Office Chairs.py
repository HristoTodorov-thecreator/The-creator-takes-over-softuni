rooms = int(input())


total = 0
for room in range(1,rooms + 1):
    chairs ,number_visitors= input().split()
    calculate_the_room = len(chairs) - int(number_visitors)
    total += calculate_the_room
    if calculate_the_room <0:
        print(f'{abs(calculate_the_room)} more chairs needed in room {room}')

if total >=0:
    print(f'Game On, {total} free chairs left')

