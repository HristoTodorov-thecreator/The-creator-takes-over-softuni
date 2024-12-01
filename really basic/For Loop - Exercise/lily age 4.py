lily_age = int(input())
washing_machine = float(input())
price_for_one_toy = int(input())

toy = 0
money = 0
monegiv = 10

for i in range (1,lily_age + 1):
    if i % 2 == 0:
        money = money + monegiv - 1
        monegiv = monegiv + 10

    else:
        toy = toy + price_for_one_toy

total_money = toy + money

if total_money >= washing_machine:
    print(f'Yes! {total_money - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_money:.2f}')