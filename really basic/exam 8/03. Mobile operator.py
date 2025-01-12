

g = input() # time contract
type_ = input() # type small middle large or extra large
internet = input()  # yes or no
for_pay = int(input()) # months for pay

internet_price = 0
total = 0
if g == 'one':
    if type_ == 'Small':
        total = 9.98
    elif type_ == 'Middle':
        total = 18.99
    elif type_ == 'Large':
        total = 25.98
    elif type_ == 'ExtraLarge':
        total = 35.99

if g == 'two':
    if type_ == 'Small':
        total = 8.58
    elif type_ == 'Middle':
        total = 17.09
    elif type_ == 'Large':
        total = 23.59
    elif type_ == 'ExtraLarge':
        total = 31.79



if total <= 10 and internet =='yes':
    internet_price = 5.50
elif 10 < total <= 30 and internet =='yes':
    internet_price = 4.35
elif total > 30 and internet =='yes':
    internet_price = 3.85



total_with_internet = total + internet_price
total_months_pay = for_pay * total_with_internet

if g == 'two':
    total_months_pay = total_months_pay - (total_months_pay * 0.0375)

print(f"{total_months_pay:.2f} lv.")


