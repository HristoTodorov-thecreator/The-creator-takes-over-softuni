from math import floor


balls = int(input())
points = 0
othercolors = 0
times_points_devided = 0

redn = 0
orangen = 0
whiten = 0
yellown = 0





for i in range(balls ):
    colors = input()
    if colors == 'red':
        points += 5
        redn += 1
    elif colors == 'orange':
        points += 10
        orangen += 1
    elif colors == 'yellow':
        points += 15
        yellown += 1
    elif colors == 'white':
        points += 20
        whiten += 1
    elif colors == 'black':
        points = points / 2
        points = floor(points)
        times_points_devided += 1
    else:
        othercolors += 1



print(f"Total points: {points}")
print(f"Red balls: {redn}")
print(f"Orange balls: {orangen}")
print(f"Yellow balls: {yellown}")
print(f"White balls: {whiten}")
print(f"Other colors picked: {othercolors}")
print(f"Divides from black balls: {times_points_devided}")

