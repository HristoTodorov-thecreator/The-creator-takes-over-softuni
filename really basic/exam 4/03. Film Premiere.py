film = input()
packet = input()
tickets = int(input())
price = 0
if film == 'John Wick':
    if packet == 'Drink':
        price = 12

    elif packet == 'Popcorn':
        price = 15

    elif packet == 'Menu':
        price = 19

elif film == 'Star Wars':
    if packet == 'Drink':
        price = 18

    elif packet == 'Popcorn':
        price = 25

    elif packet == 'Menu':
        price = 30


elif film == 'Jumanji':
    if packet == 'Drink':
        price = 9

    elif packet == 'Popcorn':
        price = 11

    elif packet == 'Menu':
        price = 14

total_ticket = price * tickets
if film == 'Star Wars' and tickets >= 4:
    total_ticket = total_ticket - (total_ticket * 0.30)
elif film == 'Jumanji' and tickets == 2:
    total_ticket = total_ticket - (total_ticket * 0.15)

print(f"Your bill is {total_ticket:.2f} leva.")




