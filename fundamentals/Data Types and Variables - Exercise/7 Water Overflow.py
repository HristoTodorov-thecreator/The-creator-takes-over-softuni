water_tank_capacity = 255

number_of_water_added = int(input())



for i in range(number_of_water_added):
    add_water = int(input())
    if water_tank_capacity - add_water < 0:
        print('Insufficient capacity!')
        continue

    water_tank_capacity -= add_water

print(f'{255 - water_tank_capacity}')



