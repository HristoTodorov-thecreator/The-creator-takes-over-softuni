

number_guests = int(input())
price_for_one_man = float(input())
budget = float(input())

if 10<= number_guests <=15:
    price_for_one_man = price_for_one_man - (price_for_one_man * 0.15)
elif 15<= number_guests <=20:
    price_for_one_man = price_for_one_man - (price_for_one_man * 0.20)
elif number_guests > 20:
    price_for_one_man = price_for_one_man - (price_for_one_man * 0.25)

cake = budget * 0.10

total_price_for_people = price_for_one_man * number_guests
total_price_for_all = total_price_for_people + cake

if budget >= total_price_for_all:
    print(f'It is party time! {budget - total_price_for_all:.2f} leva left.')
else:
    print(f'No party! {total_price_for_all - budget:.2f} leva needed.')