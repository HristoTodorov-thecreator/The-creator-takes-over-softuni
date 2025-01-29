number_days = int(input())
totallose = 0
totalwins = 0
total =0
for i in range(number_days):
    fortheday_lose = 0
    fortheday_win = 0
    total1 = 0

    while True:

        sport = input()
        if sport == 'Finish':

            break

        win_or_lose = input()
        if win_or_lose == 'win':
            total1 += 20
            totalwins += 1
            fortheday_win += 1
        else:
            totallose += 1
            fortheday_lose += 1
    if fortheday_win > fortheday_lose:
        total1 = total1 + (total1 * 0.10)
    total += total1

if totalwins > totallose:
    total = total + (total * 0.20)
if totalwins > totallose:
    print(f"You won the tournament! Total raised money: {total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total:.2f}")