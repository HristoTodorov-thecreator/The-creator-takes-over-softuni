coins = list(map(int, input().split(',')))
coins.sort(reverse=True)

target = int(input())

used_coins = {}

for coin in coins:
    if target >= coin:
        count = target // coin
        used_coins[coin] = count
        target -= count * coin

if target == 0:
    print(f'Number of coins to take: {sum(used_coins.values())}')

    for coin, count in used_coins.items():
        print(f"{count} coin(s) with value {coin}")
else:
    print("Error")