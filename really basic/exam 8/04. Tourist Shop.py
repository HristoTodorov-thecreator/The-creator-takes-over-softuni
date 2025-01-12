budget = float(input())
product = 0
total_sum_bought_products = 0
counter = 0
while True:
    name_of_the_product = input()
    if name_of_the_product == 'Stop':
        print(f"You bought {product} products for {total_sum_bought_products:.2f} leva.")
        break

    price = float(input())
    counter += 1
    if counter % 3 == 0:
        price = price / 2


    total_sum_bought_products += price

    if price > budget :
        print(f"You don't have enough money!\nYou need {price - budget:.2f} leva!")
        break
    budget -= price
    product += 1




