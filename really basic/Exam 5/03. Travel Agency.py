name_city = input()
packer_or_breakfast = input()
vip_off_price = input()
days_stay = int(input())
if days_stay <= 0:
   print(f"Days must be positive number!")
   exit()

price = 0
if name_city == 'Borovets' or name_city == 'Bansko':
    if packer_or_breakfast == 'withEquipment':
        price = 100
        if vip_off_price == 'yes':
            price = price - (price * 0.10)
    elif packer_or_breakfast == 'noEquipment':
        price = 80
        if vip_off_price == 'yes':
            price = price - (price * 0.05)
    else:
        print(f'Invalid input!')
        exit()


elif name_city == 'Varna' or name_city == 'Burgas':
    if packer_or_breakfast == 'withBreakfast':
        price = 130
        if vip_off_price == 'yes':
            price = price - (price * 0.12)
    elif packer_or_breakfast == 'noBreakfast':
        price = 100
        if vip_off_price == 'yes':
            price = price - (price * 0.07)
    else:
        print(f'Invalid input!')
        exit()




else:
    print(f'Invalid input!')
    exit()

total_ = days_stay * price
if days_stay > 7 :
    total_ = total_ - price



print(f"The price is {total_:.2f}lv! Have a nice time!")

