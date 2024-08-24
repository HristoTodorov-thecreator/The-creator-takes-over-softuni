height_house = float(input())
length = float(input())
height_roof = float(input())

green_dye = 3.4
red_dye = 4.3

window = 1.5 * 1.5
door_ = 1.2 * 2

side_wall = height_house * length
two_side_walls_total = 2 * side_wall - 2 * window
back_wall = height_house * height_house
front_with_back_wall = back_wall * 2 - door_

total_area = two_side_walls_total + front_with_back_wall
totalliters = total_area / green_dye

roofside =  2 * (length * height_house)
triangles = 2 * (height_house * height_roof /2)
total_second_area = roofside + triangles
totalliters_second = total_second_area / red_dye

print(f'{totalliters:.2f}')
print(f'{totalliters_second:.2f}')