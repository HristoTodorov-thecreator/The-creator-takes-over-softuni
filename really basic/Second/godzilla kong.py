budget_ = float(input())
numberpeople_ = int(input())
costcloth_per_man = float(input())


decor_ = budget_ * 0.10

if numberpeople_ > 150:
    costcloth_per_man = costcloth_per_man - costcloth_per_man * 0.10

totalsum_for_clothing = numberpeople_ * costcloth_per_man

moneyforfilm = totalsum_for_clothing + decor_

moneyleft = budget_ - moneyforfilm

if budget_ >= moneyforfilm:
    print("Action!")
    print(f"Wingard starts filming with {budget_ - moneyforfilm:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {moneyforfilm - budget_:.2f} leva more.")