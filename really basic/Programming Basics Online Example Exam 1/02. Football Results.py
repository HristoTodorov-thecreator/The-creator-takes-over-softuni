first_play = input()  #first football play
second_play = input()  #second football play
third_play = input()  #third football play


won_games = 0
drawn_games = 0
lost_games = 0

gm = first_play
home, away = gm.split(":")
gl = second_play
hometwo , awaytwo = gl.split(":")
gn = third_play
homethree , awaythree = gn.split(":")


int(home) , int(away) , int(hometwo) , int(awaytwo) , int(homethree) , int(awaythree)  # making integers

if home > away:  # checking the first game
    won_games = won_games + 1
elif home == away:
    drawn_games = drawn_games + 1
elif home < away:
    lost_games = lost_games + 1

if hometwo > awaytwo:  #checking the second game
    won_games = won_games + 1
elif hometwo == awaytwo:
    drawn_games = drawn_games + 1
elif hometwo < awaytwo:
    lost_games = lost_games + 1

if homethree > awaythree:  # checking the third game
    won_games = won_games + 1
elif homethree == awaythree:
    drawn_games = drawn_games + 1
elif homethree < awaythree:
    lost_games = lost_games + 1

print(f'Team won {won_games} games.')  # prints
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {drawn_games}")