
mackerel = float(input())  # mackerel for kg price
sprinkle = float(input())  # sprinkle for kg price
bonito = float(input())  # bonito kg
safrid = float(input())  # safrid kg
mussels = float(input())  # kg mussels

price_for_bonito =mackerel + mackerel * 0.60  # mackerel + 60%
safridprice = sprinkle + sprinkle * 0.80  # sprinkle + 80%
mussels_ = 7.50  # price for kg

total = mussels * mussels_ + safrid * safridprice + price_for_bonito * bonito
print(f'{total:.2f}')