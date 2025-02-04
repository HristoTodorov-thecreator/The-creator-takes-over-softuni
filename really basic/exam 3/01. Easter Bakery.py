

price_for_flour = float(input()) # for kg price
kg_flour = float(input()) # kgs
kg_sugar = float(input())
number_eggs = int(input())
packet_yeast = int(input())

sugar_price = price_for_flour - (price_for_flour * 0.25)
price_for_eggs = price_for_flour + (price_for_flour * 0.10)
yeast_price = sugar_price -(sugar_price * 0.80)

total_price_for_flour = price_for_flour * kg_flour
total_price_sugar = kg_sugar * sugar_price
total_price_eggs = number_eggs * price_for_eggs
total_yeast = packet_yeast * yeast_price

total_price = total_price_for_flour + total_price_sugar + total_price_eggs + total_yeast

print(f'{total_price:.2f}')