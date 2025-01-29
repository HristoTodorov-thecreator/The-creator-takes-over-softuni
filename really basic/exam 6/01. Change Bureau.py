number_bitcoints = int(input())
chineese_yuan = float(input())
commission = float(input())

price_for_bitcoin = 1168  # lev
price_chinesee_yuan = 0.15   # dollars
dolars = 1.76 #lev
euro = 1.95 # lev

total_bitcoin_in_lev = number_bitcoints * price_for_bitcoin
total_chineese_yuan_in_dolars = (price_chinesee_yuan * chineese_yuan) * dolars

yean_and_bit = total_chineese_yuan_in_dolars + total_bitcoin_in_lev

total = yean_and_bit / euro


percent = commission / 100

total_with_commission = total - (total * percent)

print(f'{total_with_commission:.2f}')
