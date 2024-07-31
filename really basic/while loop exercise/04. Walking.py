total = 0
goal = 10000
while total < goal:
    steps = input()

    if steps == 'Going home':
        stepsm = int(input())
        total = total + stepsm
        if total < goal:
            print(f'{abs(total - goal)} more steps to reach goal.')
            break
        else:
            print(f'Goal reached! Good job!')
            print(f'{abs(total - goal)} steps over the goal!')
            break


    total += int(steps)



    if total >= goal:
        print(f'Goal reached! Good job!')
        print(f'{total - goal} steps over the goal!')
        break



