
def stock_availability(inventory,action,*args):
    if action == 'delivery':
        inventory.extend(args)

    elif action == 'sell':
        if not args:
            inventory.pop(0)
        elif isinstance(args[0], int):
            for _ in range(args[0]):
                if inventory:
                    inventory.pop(0)
        else:
            for flavour in args:
                inventory = [box for box in inventory if box != flavour]
    return inventory



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

