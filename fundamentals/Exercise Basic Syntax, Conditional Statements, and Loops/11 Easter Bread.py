budget = float(input())
price_for_kg_flour = float(input())
one_pack_of_eggs = price_for_kg_flour * 0.75
one_liter_milk = price_for_kg_flour + (price_for_kg_flour * 0.25)

price_milk_250 = one_liter_milk / 4

price_for_loaf = price_for_kg_flour + price_milk_250 + one_pack_of_eggs

loaves = 0
colored_eggs = 0

while budget >= price_for_loaf:
    loaves += 1
    budget -= price_for_loaf

    colored_eggs += 3

    if loaves % 3 ==0:
        colored_eggs -= (loaves -2)

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')