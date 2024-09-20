month = input()
day = int(input())

totalone = 0
total = 0

if month == 'May' or month == 'October':
    totalone = day * 50
    total = day * 65
    if day > 14:
        total = total - (total * 0.10)

    if day > 14:
        totalone = totalone - (totalone * 0.30)
    elif day > 7:
        totalone = totalone - (totalone * 0.05)

elif month == 'June' or month == 'September':
    totalone = day * 75.20
    total = day * 68.70
    if day > 14:
        total = total - (total * 0.10)
        totalone = totalone - (totalone * 0.20)

elif month == 'July' or month == 'August':
    totalone = day * 76
    total = day * 77
    if day > 14:
        total = total - (total * 0.10)

print(f"Apartment: {total:.2f} lv.")
print(f"Studio: {totalone:.2f} lv.")