money_needed_for_vacation = float(input())
saved_money = float(input())
maxdays = 5

days = 0
days_spend = 0
while days_spend < maxdays:
    spend = input()  # save or spend
    sumtotal = float(input())
    days = days + 1
    if spend == 'spend':
        saved_money = saved_money - sumtotal if saved_money > sumtotal else 0
        days_spend = days_spend + 1
    if spend == 'save':
        saved_money = saved_money + sumtotal
        days_spend = 0





    if saved_money >= money_needed_for_vacation:
        print(f"You saved the money for {days} days.")
        break
else:
    print(f"You can't save the money.")
    print(f"{days}")

