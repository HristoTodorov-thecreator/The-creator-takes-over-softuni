
bestplayer =''
most_goals = 0
while True:
    player_name = input()
    if player_name == 'END':
        break
    goals = int(input())

    if goals > most_goals:
        most_goals = goals
        bestplayer = player_name
    if goals >= 10:
        break

print(f"{bestplayer} is the best player!")

if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")


