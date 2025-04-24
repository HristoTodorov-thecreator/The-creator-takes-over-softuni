
matrix = []
for _ in range(6):
    row = input().split()
    matrix.append(row)


initial_pos = input()
row, col = map(int, initial_pos.strip("()").split(", "))


while True:
    command_input = input().split(", ")
    command = command_input[0]
    if command == "Stop":
        break

    direction = command_input[1]


    new_row, new_col = row, col
    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1


    if command == "Create":
        value = command_input[2]
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = value
    elif command == "Update":
        value = command_input[2]
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = value
    elif command == "Delete":
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = "."
    elif command == "Read":
        if matrix[new_row][new_col] != ".":
            print(matrix[new_row][new_col])


    row, col = new_row, new_col


for row in matrix:
    print(" ".join(row))