eggs_we_have = int(input())
eggs_sold = 0
while True:
    buy_or_fill = input()


    if buy_or_fill =='Close':
        print(f"Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break
    amount = int(input())


    if buy_or_fill == 'Buy':
        if amount > eggs_we_have:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_we_have}.")
            break

        else:
             eggs_we_have -= amount
             eggs_sold += amount
    elif buy_or_fill == 'Fill':
        eggs_we_have += amount