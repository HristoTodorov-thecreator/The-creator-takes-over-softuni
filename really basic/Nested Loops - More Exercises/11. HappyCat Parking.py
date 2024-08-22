number_days = int(input())
hours_a_day = int(input())
total = 0
day = 0
price = 0
for i in range (1,number_days + 1):
    total2 = 0

    for k in range (1,hours_a_day + 1):
        if i % 2 == 0 and k % 2 != 0:
            price = 2.50
        elif i % 2 != 0 and k % 2 == 0:
            price = 1.25
        else:
            price = 1.00

        total += price
        total2 += price

    day += 1
    print(f"Day: {day} - {total2:.2f} leva")

print(f"Total: {total:.2f} leva")
