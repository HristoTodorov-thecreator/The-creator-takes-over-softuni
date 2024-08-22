num_money_1_lv = int(input())
num_money_2_lv = int(input())
num_money_5_lv = int(input())

sum_ = int(input())

for i in range (num_money_1_lv +1):
    for k in range (num_money_2_lv +1):
        for s in range (num_money_5_lv + 1):
            if i * 1 + k * 2 + s * 5 == sum_:
                print(f'{i} * 1 lv. + {k} * 2 lv. + {s} * 5 lv. = {sum_} lv.')

