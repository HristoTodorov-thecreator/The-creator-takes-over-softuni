from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]

customers = deque([int(x) for x in input().split(', ')])


while customers and bowls_of_ramen:
    last_bowl = bowls_of_ramen.pop()
    first_customer = customers.popleft()

    if last_bowl == first_customer:
        continue
    elif last_bowl > first_customer:
        last_bowl -= first_customer
        bowls_of_ramen.append(last_bowl)
    else:
        first_customer -= last_bowl
        customers.appendleft(first_customer)


if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str,bowls_of_ramen))}")

else:
    print(f"Out of ramen! You didn't manage to serve all customers.")

    print(f"Customers left: {', '.join(map(str,customers))}")
