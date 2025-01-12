

strawberry = float(input()) # price for strawberry
kg_banana = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

strawberrytotal = strawberry_kg * strawberry
raspberries_price_for_kg = strawberry / 2
totalraspberries = raspberries_kg * raspberries_price_for_kg
orange_price_for_kg = raspberries_price_for_kg - ( raspberries_price_for_kg  * 0.40)
totalpricefororange = orange_price_for_kg * orange_kg
price_for_bananas_for_kg = raspberries_price_for_kg - (raspberries_price_for_kg * 0.80)
total_price_for_bananas = price_for_bananas_for_kg * kg_banana

total_for_all = strawberrytotal + totalraspberries + totalpricefororange + total_price_for_bananas
print(f'{total_for_all:.2f}')

