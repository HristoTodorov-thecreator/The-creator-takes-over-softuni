

chrysanthemums = int(input()) #number
rose = int(input()) #number
tulips = int(input()) #number
season = input()
holiday = input()


arrangement = 2

pricerose = 0
pricetulips = 0
pricechrysanthemums = 0

totalnumber = rose + tulips + chrysanthemums

price = 0
if season == 'Summer' or season == 'Spring':
    pricerose = 4.10
    pricetulips = 2.50
    pricechrysanthemums = 2
elif season == 'Winter' or season == 'Autumn':
    pricerose = 4.50
    pricetulips = 4.15
    pricechrysanthemums = 3.75

total = pricerose * rose + pricetulips * tulips + pricechrysanthemums * chrysanthemums

if holiday == 'Y':
    total = total + (total * 0.15)

if tulips > 7 and season == 'Spring':
    total = total - (total * 0.05)

if rose >= 10 and season == 'Winter':
    total = total - (total * 0.10)


if totalnumber > 20:
    total = total - (total * 0.20)

total_with_arr = total + arrangement
print(f'{total_with_arr:.2f}')
