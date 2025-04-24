quantity_of_decorations = int(input())
days_left_until_chr = int(input())

Ornament_price_set_piece = 2 #$
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_cost = 0
total_spirit = 0



for i in range(1,days_left_until_chr + 1):
    if i % 11 ==0:
        quantity_of_decorations += 2
    if i % 2 ==0:
        total_cost += quantity_of_decorations * Ornament_price_set_piece
        total_spirit += 5
    if i % 3 == 0:
        total_cost +=quantity_of_decorations * tree_garland
        total_cost += quantity_of_decorations * tree_skirt
        total_spirit += 3
        total_spirit += 10

    if i % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights
        total_spirit += 17
        if days_left_until_chr % 3 ==0:
            total_spirit += 30
    if i % 10 ==0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights


if days_left_until_chr % 10 ==0:
    total_spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')





