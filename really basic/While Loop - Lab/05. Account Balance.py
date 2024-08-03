total = 0
while True:
    money = input()
    if money == 'NoMoreMoney':
        print(f'Total: {total:.2f}')
        break
    summoney = float(money)
    if summoney <= 0:
        print(f'Invalid operation!')
        print(f'Total: {total:.2f}')
        break



    total += summoney
    print(f'Increase: {summoney:.2f}')
