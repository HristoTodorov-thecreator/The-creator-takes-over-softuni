from collections import deque


food = int(input())


orders = deque([int(x) for x in input().split()])


print(max(orders))


while orders:
    if orders[0] > food:
        break
    else:
        food -= orders.popleft()

if orders:
    print(f'Orders left:',*orders)
else:
    print(f'Orders complete')