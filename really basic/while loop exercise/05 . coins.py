number = float(input())# if 1.25
g = int(number * 100)  # 1.25 * 100 = 125 coins
totalremoves = 0
while g > 0:



    if g >= 200:
        g = g - 200

    elif g >= 100:
        g = g - 100

    elif g >= 50:
        g = g - 50

    elif g >= 20:
        g = g - 20

    elif g >= 10:
        g = g - 10

    elif g >= 5:
        g = g - 5

    elif g >= 2:
        g = g - 2

    elif g >= 1:
        g = g - 1

    totalremoves += 1

    if g == 0:
        print(f'{totalremoves}')





