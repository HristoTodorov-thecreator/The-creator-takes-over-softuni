type_final = input()  # Quarter final ”, “Semi final” ,“Final”
type_ticket = input()  # “Standard”, “Premium”, “VIP”
number_of_ticket = int(input())
picture = input()  # Y OR N

total = 0
trophy_pic_price = 40

if type_final == 'Quarter final':
    if type_ticket == 'Standard':
        total = number_of_ticket * 55.50
    elif type_ticket == 'Premium':
        total = number_of_ticket * 105.20
    elif type_ticket == 'VIP':
        total = number_of_ticket * 118.90

elif type_final == 'Semi final':
    if type_ticket == 'Standard':
        total = number_of_ticket * 75.88
    elif type_ticket == 'Premium':
        total = number_of_ticket * 125.22
    elif type_ticket == 'VIP':
        total = number_of_ticket * 300.40

elif type_final == 'Final':
    if type_ticket == 'Standard':
        total = number_of_ticket * 110.10
    elif type_ticket == 'Premium':
        total = number_of_ticket * 160.66
    elif type_ticket == 'VIP':
        total = number_of_ticket * 400

if total > 4000:
      total = total - (total * 0.25)
      trophy_pic_price = 0
elif total > 2500:
    total = total - (total * 0.10)

if picture == "N":
    trophy_pic_price = 0
elif picture == "Y":
    trophy_pic_price = trophy_pic_price * number_of_ticket
elif picture == "Y" and total > 4000:
    trophy_pic_price = 0


totalpay = trophy_pic_price + total
print(f'{totalpay:.2f}')
