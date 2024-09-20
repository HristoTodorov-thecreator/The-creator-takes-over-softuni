Budget = float(input())
Season = input()  # winter or summer

total = 0


if Budget <= 100:
    if Season == 'winter':
        total = Budget * 0.70
        print("Somewhere in Bulgaria")
        print(f"{'Hotel'} - {total:.2f}")
    elif Season == 'summer':
        total = Budget * 0.30
        print("Somewhere in Bulgaria")
        print(f"{'Camp'} - {total:.2f}")

elif Budget <= 1000:
    if Season == 'winter':
        total = Budget * 0.80
        print("Somewhere in Balkans")
        print(f"{'Hotel'} - {total:.2f}")
    elif Season == 'summer':
        total = Budget * 0.40
        print("Somewhere in Balkans")
        print(f"{'Camp'} - {total:.2f}")
elif Budget > 1000:
    if Season == 'winter':
        total = Budget * 0.90
        print("Somewhere in Europe")
        print(f"{'Hotel'} - {total:.2f}")
    elif Season == 'summer':
        total = Budget * 0.90
        print("Somewhere in Europe")
        print(f"{'Hotel'} - {total:.2f}")