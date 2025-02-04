easter_bread = 3.20
eggs = 4.35
cookie = 5.40 # for kg
paint_for_eggs = 0.15 # for egg

number_easter_bread = int(input())
number_eggs = int(input())
number_kg_cookies = int(input())

total_easter_bread_pr = easter_bread * number_easter_bread
total_eggs_price = eggs * number_eggs
total_cookies = cookie * number_kg_cookies

eggs_S = number_eggs * 12
price_for_paint = eggs_S * paint_for_eggs

total_for_all = total_easter_bread_pr + total_eggs_price + total_cookies + price_for_paint

print(f'{total_for_all:.2f}')