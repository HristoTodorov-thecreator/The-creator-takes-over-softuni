rows,cols = input().split()
rows = int(rows)
cols = int(cols)

row , col = 0,0

moves = 0
touched = 0
matrix = []
for i in range(rows):
    data = input().split()
    for s in range(cols):

        if data[s] == 'B':
            row,col = i,s

    matrix.append(data)


directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

while True:
    command = input()
    if command == "Finish" or touched >= 3:
        break

    if command not in directions:
        continue

    dr, dc = directions[command]
    new_row, new_col = row + dr, col + dc


    if not (0 <= new_row < rows and 0 <= new_col < cols):
        continue
    if matrix[new_row][new_col] == 'O':
        continue


    moves += 1


    if matrix[new_row][new_col] == 'P':
        touched += 1
        matrix[new_row][new_col] = '-'


    row, col = new_row, new_col

print(f"Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")

