from sys import maxsize
biggestnum = - maxsize
color = ''

eggs = int(input())
orange = 0
blue = 0
red = 0
green = 0



for i in range (eggs ):
    egg_color = input()
    if egg_color ==  'red':
        red += 1

    elif egg_color == 'blue':
        blue += 1

    elif egg_color == 'green':
        green += 1

    elif egg_color == 'orange':
        orange += 1

    if orange > biggestnum:
        biggestnum = orange
        color ='orange'
    if blue > biggestnum:
        biggestnum = blue
        color ='blue'
    if red > biggestnum:
        biggestnum = red
        color ='red'
    if green > biggestnum:
        biggestnum = green
        color ='green'

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {biggestnum} -> {color}")
