from math import floor
from math import ceil

The_vineyard = int(input())  # vineyard square meters
grapes = float(input())  # grapes per square meter
liters_wine = int(input())  # needed liters
workers = int(input()) # workers number

totalgrapes = The_vineyard * grapes
winetotal = (totalgrapes * 0.40 ) / 2.5

wine_left = abs(winetotal - liters_wine)
forone_ = wine_left / workers  # wine for one worker




if winetotal >= liters_wine:
    print(f'Good harvest this year! Total wine: {floor(winetotal)} liters.')
    print(f"{ceil(wine_left)} liters left -> {ceil(forone_)} liters per person.")
else:
    print(f'It will be a tough winter! More {floor(wine_left)} liters wine needed.')

