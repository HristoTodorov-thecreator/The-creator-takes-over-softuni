intervals = int(input())

number = 0
total = 0

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 =0
invalid =0




for i in range (intervals):
    g = int(input())
    if 0 <= g <= 9:
        number = g * 0.20
        total += number
        from_0_to_9 += 1


    elif 10 <= g <= 19:
        number = g * 0.30
        total += number
        from_10_to_19 += 1

    elif 20 <= g <= 29:
        number = g * 0.40
        total += number
        from_20_to_29 +=1

    elif 30 <= g <= 39:
        number = 50
        total += number
        from_30_to_39 += 1

    elif 40 <= g <= 50:
        number = 100
        total += number
        from_40_to_50 += 1


    else:
        total = total / 2
        invalid += 1


print(f'{total:.2f}')
print(f"From 0 to 9: {from_0_to_9 / intervals * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19/ intervals * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / intervals * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / intervals * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / intervals * 100:.2f}%")
print(f"Invalid numbers: {invalid / intervals * 100:.2f}%")