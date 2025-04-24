player_one,player_two = input().split(', ')
matrix = []
for i in range(6):
    maze = input().split()
    matrix.append(maze)

players = {player_one:(0,0),player_two:(0,0)}

p1 = False
p2 = False

while True:

    new_row,new_col = map(int,input().strip("()").split(', '))

    if player_one == 'Tom' and p1:
        player_one, player_two = player_two, player_one
        p1 = False
        continue

    if player_one == 'Jerry' and p2:
        player_one, player_two = player_two, player_one
        p2 = False
        continue

    if matrix[new_row][new_col] == "E":
        print(f"{player_one} found the Exit and wins the game!" )
        break
    elif matrix[new_row][new_col] == 'T':
        print(f"{player_one} is out of the game! The winner is {player_two}.")
        break

    elif matrix[new_row][new_col] == 'W':
        print(f"{player_one} hits a wall and needs to rest.")
        if player_one == 'Tom':
            p1 = True
        elif player_one == 'Jerry':
            p2 = True







    player_one,player_two = player_two,player_one




