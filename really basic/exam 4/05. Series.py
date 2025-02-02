budget = float(input())
number_serials = int(input())
total = 0
for i in range (number_serials):
    name_serial = input()
    price = float(input())

    if name_serial == 'Thrones':
        price = price - (price * 0.50)
    elif name_serial == 'Lucifer':
        price = price - (price * 0.40)
    elif name_serial == 'Protector':
        price = price - (price * 0.30)
    elif name_serial == 'TotalDrama':
        price = price - (price * 0.20)
    elif name_serial == 'Area':
        price = price - (price * 0.10)

    total += price

if budget >= total:
    print(f"You bought all the series and left with {budget - total:.2f} lv.")
else:
    print(f"You need {total - budget:.2f} lv. more to buy the series!")



