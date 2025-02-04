customers = int(input())
totalforall = 0
price = 0

for i in range(customers):
    item_ = 0

    total = 0
    while True:
        item = input()
        if item == 'Finish':
            if item_ % 2 == 0:
                total = total - (total * 0.20)
            totalforall += total
            print(f'You purchased {item_} items for {total:.2f} leva.')
            break
        else:
            item_ += 1
            if item == 'basket':
                price = 1.50
            elif item == 'wreath':
                price = 3.80
            elif item == 'chocolate bunny':
                price = 7


        total += price



print(f'Average bill per client is: {totalforall / customers:.2f} leva.')