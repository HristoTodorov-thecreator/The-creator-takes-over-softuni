def shopping_cart(*args):
    meal_limits = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    cart = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }

    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg
        if len(cart[meal]) < meal_limits[meal]:
            cart[meal].add(product)


    total_products = sum(len(products) for products in cart.values())
    if total_products == 0:
        return "No products in the cart!"


    sorted_meals = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for meal, products in sorted_meals:
        meal_entry = f"{meal}:"
        if products:
            sorted_products = sorted(products)
            for product in sorted_products:
                meal_entry += f"\n - {product}"
        result.append(meal_entry)

    return "\n".join(result)