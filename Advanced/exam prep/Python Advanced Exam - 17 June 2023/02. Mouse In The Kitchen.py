rows, cols = input().split(',')
rows = int(rows)
cols = int(cols)
matrix = []

cheese = 0
row, col = 0, 0

for i in range(rows):
    data = input()
    for s in data:
        if s == 'M':
            row, col = i, data.index(s)
        if s == 'C':
            cheese += 1
    matrix.append(list(data))

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

command = input()
while command != "danger" and cheese > 0:
    if command in directions:
        dr, dc = directions[command]
        new_row, new_col = row + dr, col + dc


        if not (0 <= new_row < rows and 0 <= new_col < cols):
            print("No more cheese for tonight!")
            break


        if matrix[new_row][new_col] == '@':
            command = input()
            continue


        matrix[row][col] = '*'


        if matrix[new_row][new_col] == 'T':
            matrix[new_row][new_col] = 'M'
            print("Mouse is trapped!")
            break


        if matrix[new_row][new_col] == 'C':
            cheese -= 1
            if cheese == 0:
                matrix[new_row][new_col] = 'M'
                print("Happy mouse! All the cheese is eaten, good night!")
                break


        matrix[new_row][new_col] = 'M'
        row, col = new_row, new_col

    command = input()


if command == "danger" and cheese > 0:
    print("Mouse will come back later!")

for row in matrix:
    print(''.join(row))