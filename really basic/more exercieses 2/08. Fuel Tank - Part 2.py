type_fuel = input()
liters_fuel = float(input())
card = input()

gas = 0.93 # for liter
gasoline = 2.22 #for liter
diesel = 2.33 # for liter
price = 0
if type_fuel == 'Gas':
    price = gas
    if card == 'Yes':
        price = price - 0.08

elif type_fuel == 'Diesel':
    price = diesel
    if card == 'Yes':
        price = price - 0.12


elif type_fuel == 'Gasoline':
    price = gasoline
    if card == 'Yes':
        price = price - 0.18

total = price * liters_fuel

if 20 <= liters_fuel <= 25:
    total = total - (total * 0.08)
elif liters_fuel > 25:
    total = total - (total * 0.10)

print(f"{total:.2f} lv.")


