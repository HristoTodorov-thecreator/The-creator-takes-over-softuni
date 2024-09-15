from math import ceil
from math import floor


rose = 3.50

magnolias = 3.25

hyacinths = 4

cactus = 8

number_magnolias = int(input())
number_hyacinths = int(input())
number_rose = int(input())
number_cactus = int(input())
price_gift = float(input())

totalmagn = number_magnolias * magnolias
totalhyacin = number_hyacinths * hyacinths
totalrose = number_rose * rose
totalcac = number_cactus * cactus

total = totalmagn + totalhyacin + totalrose + totalcac

total_with_tax = total - (total * 0.05)

if total_with_tax >= price_gift:
    print(f"She is left with {floor(total_with_tax - price_gift)} leva.")
else:
    print(f"She will have to borrow {ceil(price_gift - total_with_tax)} leva.")