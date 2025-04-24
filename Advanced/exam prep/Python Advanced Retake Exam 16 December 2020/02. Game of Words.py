string = input()

size_matrix = int(input())



matrix = []

row,col = 0,0

for i in range(size_matrix):
    data = list(input())
    matrix.append(data)


    if 'P' in data:
        row,col = i,data.index('P')

number_m = int(input())




directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
for s in range(number_m):
    command = input()
    move = directions[command]
    new_row,new_col = row + move[0],col + move[1]
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        matrix[row][col] = '-'
        if matrix[new_row][new_col].isalpha():
            string += matrix[new_row][new_col]

        row, col = new_row, new_col
        matrix[row][col] = "P"


    else:
        string = string[:-1]

print(string)

for data in matrix:
    print(''.join(data))