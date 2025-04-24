days_plunder = int(input())
daily_plunder = int(input())
expected = float(input())

collected = 0
for i in range(1,days_plunder + 1):

    if i % 3 ==0:
        collected += daily_plunder + (daily_plunder *0.50)
    else:
        collected += daily_plunder

    if i % 5 ==0:
        collected -= (collected *0.30)


if collected >= expected:
    print(f'Ahoy! {collected:.2f} plunder gained.')
else:
    print(f'Collected only {(collected / expected) * 100:.2f}% of the plunder.')

