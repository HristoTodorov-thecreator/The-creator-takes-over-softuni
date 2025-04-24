size = int(input())

matrix = []
player_pos = []
coins = 0

path = []

for row in range(size):
    info = input().split()
    matrix.append(info)
    for s in range(size):
        if matrix[row][s] == 'P':
            player_pos = [row,s]
            matrix[row][s] = '0'
            path.append([row,s])


def move_player(row,col):
    if row < 0:
        row = size - 1  # if he exited with direction up he goes down
    elif row >= size:
        row = 0  # if he exited with direction down he goes up
    if col < 0:
        col = size - 1  # if he exited with direction left he goes right
    elif col >= size:
        col = 0  # # if he exited right he goes left
    return row, col






while True:
    command = input()
    if command not in ("up", "down", "left", "right"):
        continue

    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    move = directions[command]

    player_pos[0],player_pos[1] = move_player(player_pos[0] + move[0], player_pos[1] + move[1])

    path.append((player_pos[0],player_pos[1]))

    if matrix[player_pos[0]][player_pos[1]] == "X":
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(matrix[player_pos[0]][player_pos[1]])
    matrix[player_pos[0]][player_pos[1]] = "0"

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
for step in path:
    print(f"[{step[0]}, {step[1]}]")



