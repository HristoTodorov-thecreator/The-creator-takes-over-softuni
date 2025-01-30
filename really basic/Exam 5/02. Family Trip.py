
budget = float(input())
overnight_stay_days = int(input())
price_for_overnight_stay = float(input())
percent_add_cost = int(input())

if overnight_stay_days > 7 :
    price_for_overnight_stay = price_for_overnight_stay - (price_for_overnight_stay * 0.05)

price_ = overnight_stay_days * price_for_overnight_stay

the_add_cost = budget * (percent_add_cost / 100)
total = price_ + the_add_cost

if budget >= total:
    print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")
else:
    print(f"{total - budget:.2f} leva needed.")

