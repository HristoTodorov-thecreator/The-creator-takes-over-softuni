highest_score = 0
player = ''

while True:
    name = input()
    if name == 'Stop':
        break
    n = len(name)
    score = 0
    for i in range(n):
        number = int(input())
        if number == ord(name[i]):
            score += 10
        else:
            score += 2
        if score >= highest_score:
            highest_score = score
            player = name



print(f"The winner is {player} with {highest_score} points!")