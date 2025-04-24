from collections import deque

row,col = 0,0
matrix = []
for i in range(6):
    data = input().split()
    matrix.append(data)
    for s in range(6):
        if matrix[i][s] == 'E':
            row,col = i,s

water,concrete,metal =0,0,0
commands = deque(input().split(', '))
while commands:
    command = commands.popleft()


    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    for c_pos, n_pos in ((-1, 5), (6, 0)):
        if col == c_pos:
            col = n_pos
        if row == c_pos:
            row = n_pos

    if matrix[row][col] == "R":
        print(f'Rover got broken at ({row}, {col})')
        break
    if matrix[row][col] == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")


if metal and water and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



