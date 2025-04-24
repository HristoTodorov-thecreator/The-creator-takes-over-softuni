thebudget = int(input())

l = 0


while True:
    price = input()
    if price == 'End':
        print(f'You bought everything needed.')
        break
    g = int(price)
    l += g
    if l > thebudget:
        print(f'You went in overdraft!')
        break