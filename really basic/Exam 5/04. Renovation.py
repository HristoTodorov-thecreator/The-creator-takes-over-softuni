from math import ceil
high_wall = int(input())
witdh_wall = int(input())
no_paint_wall_percent = int(input())

paint_it = input()

total_room_size = ceil((high_wall * witdh_wall * 4) * (1 - no_paint_wall_percent / 100 ))
while paint_it != 'Tired!':
    paint_it = int(paint_it)

    total_room_size -= paint_it
    if total_room_size < 0:
        print(f'All walls are painted and you have {abs(total_room_size)} l paint left!')
        break
    if total_room_size == 0:
        print("All walls are painted! Great job, Pesho!" )
        break

    paint_it = input()

else:
    print(f'{total_room_size} quadratic m left.')