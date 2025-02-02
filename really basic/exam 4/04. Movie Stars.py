budget = float(input())

while True:
    name_actor = input()
    if name_actor == 'ACTION':
        if budget >= 0 :
            print(f'We are left with {abs(budget):.2f} leva.')
        else:
            print(f'We need {abs(budget):.2f} leva for our actors.')
        break
    if len(name_actor) > 15:
        budget = budget - (budget * 0.20)
    else:
        pay = float(input())
        budget -= pay

    if budget < 0:
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break

