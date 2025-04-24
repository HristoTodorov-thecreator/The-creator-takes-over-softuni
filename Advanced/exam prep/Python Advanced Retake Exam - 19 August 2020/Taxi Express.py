
from collections import deque
customers = deque([int(x) for x in input().split(', ')]) # times for destinations

taxis_nums = [int(x) for x in input().split(', ')] # how much time they can drive


total_time = 0
while customers and taxis_nums:
    customer = customers.popleft()
    taxi = taxis_nums.pop()

    if taxi >= customer:
        total_time += customer

    else:
        customers.appendleft(customer)

if not customers:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

if not taxis_nums and customers:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str,customers))}')
