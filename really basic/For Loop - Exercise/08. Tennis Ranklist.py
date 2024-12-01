from math import floor
tournament = int(input())
startup_points = int(input())

points = 0

wintournaments = 0
for _ in range (tournament):
    tournament_type = input()
    if tournament_type == 'W':
        points += 2000
        wintournaments += 1
    elif tournament_type == 'F':
        points += 1200
    elif tournament_type == 'SF':
        points += 720


avaragep = points / tournament
points = points + startup_points


win_percentage = (wintournaments / tournament) * 100

print(f'Final points: {points}')
print(f'Average points: {floor(avaragep)}')
print(f'{win_percentage:.2f}%')