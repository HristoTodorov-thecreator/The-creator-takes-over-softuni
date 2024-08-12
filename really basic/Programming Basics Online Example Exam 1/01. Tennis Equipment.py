from math import floor
from math import ceil



tennis_racket = float(input())  # price for one
number_tennis_rackets = int(input())
shoes = int(input())  # number of shoes

total_price_tennis_racket = number_tennis_rackets * tennis_racket
shoes_price = tennis_racket / 6
total_shoe_price = shoes * shoes_price

equipment = (total_shoe_price + total_price_tennis_racket) * 0.20

total_price_for_everything = total_shoe_price + total_price_tennis_racket + equipment

price_for_Djokovic = total_price_for_everything / 8

price_for_sponsors = total_price_for_everything * 7/8

print(f"Price to be paid by Djokovic {floor(price_for_Djokovic)}")
print(f"Price to be paid by sponsors {ceil(price_for_sponsors)}")