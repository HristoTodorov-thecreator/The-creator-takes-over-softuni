from math import ceil
from sys import maxsize

biggsugar = - maxsize
bigflour = - maxsize
g = int(input())

totalsugar = 0
totalflour = 0

for i in range (g):
    sugar = int(input())
    flour = int(input())
    totalsugar += sugar
    totalflour += flour

    if sugar > biggsugar:
        biggsugar = sugar
    if flour > bigflour:
        bigflour = flour



packetsugar = totalsugar / 950
packetflour = totalflour / 750
fr = ceil(packetsugar)
gr = ceil(packetflour)

print(f'Sugar: {fr}')
print(f'Flour: {gr}')
print(f"Max used flour is {bigflour} grams, max used sugar is {biggsugar} grams.")
