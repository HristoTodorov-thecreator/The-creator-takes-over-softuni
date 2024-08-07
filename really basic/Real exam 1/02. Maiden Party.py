lovemessage = 0.60
rose = 7.20
keychain = 3.60
caricature = 18.20
lucky_price = 22

price_for_the_party = float(input())
number_love_messages = int(input())
number_roses = int(input())
number_key_chains = int(input())
number_caricatures = int(input())
num_lucky_suprices = int(input())

totalsum =( number_love_messages * lovemessage + number_roses * rose + number_key_chains * keychain + number_caricatures
* caricature + num_lucky_suprices * lucky_price )  # total price for purchases

number_bought_items = number_love_messages + number_roses + number_key_chains + number_caricatures + num_lucky_suprices

if number_bought_items >= 25 :
    totalsum = totalsum - (totalsum * 0.35)  # percent discount

totalwithhosting = totalsum - (totalsum * 0.10)  # goes 10% for hosting


if totalwithhosting >= price_for_the_party:

    print(f"Yes! {totalwithhosting - price_for_the_party:.2f} lv left.")
else:

    print(f"Not enough money! {price_for_the_party - totalwithhosting:.2f} lv needed.")
