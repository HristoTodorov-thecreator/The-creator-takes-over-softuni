items = input().replace('->',' ').replace('|',' ')
g = items.split()

budget = float(input())
ticket_for_france = 150


money_for_shopping = 0
money_from_selling = 0
list_ = []



for i in range(0, len(g), 2):
    item = g[i]
    price = g[i + 1]
    t = float(price)

    if budget < t:
        continue


    if item == 'Clothes' and t <= 50:
        budget -= t
        selling_price = t + (t * 0.40)
        money_for_shopping += t
        money_from_selling += selling_price
        list_.append(f'{selling_price:.2f}')
    elif item == 'Shoes' and t <= 35:
        budget -= t
        selling_price = t + (t * 0.40)
        money_for_shopping += t
        money_from_selling += selling_price
        list_.append(f'{selling_price:.2f}')
    elif item == 'Accessories' and t <= 20.50:
        budget -= t
        selling_price = t + (t * 0.40)
        money_for_shopping += t
        money_from_selling += selling_price
        list_.append(f'{selling_price:.2f}')


print(' '.join(list_))
print(f'Profit: {money_from_selling - money_for_shopping:.2f}')

budget += money_from_selling
if budget >= ticket_for_france:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')











