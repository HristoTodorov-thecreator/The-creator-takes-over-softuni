wanted_profit = float(input())
total = 0
while True:

    drink = input()
    if drink == 'Party!':
        print(f"We need {wanted_profit - total:.2f} leva more.")
        print(f'Club income - {total:.2f} leva.')
        break
    number_drinks = int(input())
    g = len(drink)
    result = number_drinks * g
    if result % 2 != 0:
        result = result - (result * 0.25)
    total += result




    if total >= wanted_profit:
        print(f"Target acquired.")
        print(f"Club income - {total:.2f} leva.")
        break