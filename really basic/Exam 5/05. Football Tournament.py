name_club = input()
number_played_games = int(input())

win_games = 0
lost_games = 0
draw_games = 0
points = 0



for i in range (number_played_games):


    g = input()
    if g == 'W':
        win_games += 1
        points += 3

    elif g == 'D':
        draw_games += 1
        points += 1

    elif g == 'L':
        lost_games += 1

if number_played_games == 0:
    print(f"{name_club} hasn't played any games during this season.")
    exit()
print(f'{name_club} has won {points} points during this season.')
print(f"Total stats:")
print(f'## W: {win_games}')
print(f'## D: {draw_games}')
print(f'## L: {lost_games}')
print(f'Win rate: {(win_games / number_played_games) * 100:.2f}%')

