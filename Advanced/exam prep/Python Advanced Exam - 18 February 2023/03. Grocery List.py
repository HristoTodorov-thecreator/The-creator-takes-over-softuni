

def shop_from_grocery_list(budget,products_needed,*args):
    buyed_products = []
    the_budget = budget

    for product,price in args:
        if price > the_budget:
            break

        if product in products_needed and product not in buyed_products:
            buyed_products.append(product)
            the_budget -= price

    missing_products = [item for item in products_needed if item not in buyed_products]

    if not missing_products:
        return f"Shopping is successful. Remaining budget: {the_budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))