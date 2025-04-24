def shopping_list(budget,**kwargs):
    shopping_cart = set()
    result = []

    if budget < 100:
        return "You do not have enough budget."



    for product,value in kwargs.items():


        if len(shopping_cart) >=5:
            break
        price,quan = value
        total = price * quan
        if budget >= total:
            budget -= total
            shopping_cart.add(product)
            result.append(f'You bought {product} for {total:.2f} leva.')
        else:
            continue

    return "\n".join(result)




print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))