voucher = int(input())


for_consumption = 0
film = 0
while True:
    what_he_want = input()

    if what_he_want == 'End':
        print(f'{film}')
        print(f'{for_consumption}')
        break
    price = 0
    if len(what_he_want) > 8:
        price = ord(what_he_want[0]) + ord(what_he_want[1])
    else:
        price = ord(what_he_want[0])


    if voucher >= price:
        voucher -= price
    elif price > voucher:
        print(f'{film}')
        print(f'{for_consumption}')
        break
    if len(what_he_want) > 8:
        film += 1
    else:
        for_consumption += 1