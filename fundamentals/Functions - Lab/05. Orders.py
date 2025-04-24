
what_is_the_order = input()
number = int(input())

price = 0

if what_is_the_order == 'water':
    price = 1.00
elif what_is_the_order == 'coffee':
    price = 1.50
elif what_is_the_order == 'coke':
    price = 1.40
elif what_is_the_order == 'snacks':
    price = 2.00






def orders():
    def the_order():
        result = lambda a , b: a * b
        g = result(price , number)
        return g
    return the_order()


t = orders()
print(f'{t:.2f}')



