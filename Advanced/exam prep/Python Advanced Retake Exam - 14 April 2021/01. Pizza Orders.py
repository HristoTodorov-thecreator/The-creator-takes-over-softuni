from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])

employee_capacity = [int(x) for x in input().split(', ')]

total = 0
while pizza_orders and employee_capacity:
    first_pizza = pizza_orders.popleft()
    last_emp = employee_capacity.pop()
    if not(0 < first_pizza < 11):
        employee_capacity.append(last_emp)
        continue

    if first_pizza > last_emp:
        result = first_pizza - last_emp
        pizza_orders.appendleft(result)
        total += last_emp
    else:
        result = last_emp - first_pizza
        total += first_pizza


if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total}')
    print(f'Employees: {", ".join(map(str,employee_capacity))}')

if not employee_capacity and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str,pizza_orders))}")