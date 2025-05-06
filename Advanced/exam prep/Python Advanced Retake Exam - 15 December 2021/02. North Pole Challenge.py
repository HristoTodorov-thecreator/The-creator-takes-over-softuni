rows,cols = input().split(', ')
rows = int(rows)
cols = int(cols)

row,col = 0,0
matrix= []
items_left = 0
for i in range(rows):
    data = input().split()
    matrix.append(data)

    for s in range(cols):
        if matrix[i][s] == 'Y':
            row,col = i,s
        if matrix[i][s] == 'D':
            items_left += 1
        elif matrix[i][s] == 'G':
            items_left += 1
        elif matrix[i][s] == 'C':
            items_left += 1



collected = {"D": 0, "G": 0, "C": 0}


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == 'End':
        break

    direction,steps = command.split('-')
    steps = int(steps)

    for _ in range(steps):
        matrix[row][col] = "x"

        dr, dc = directions[direction]

        row = (row + dr) % rows
        col = (col + dc) % cols

        current = matrix[row][col]
        if current in collected:
            collected[current] += 1
            items_left -= 1

        matrix[row][col] = "Y"

        if items_left == 0:
            print("Merry Christmas!")
            break

    if items_left == 0:
        break


print("You've collected:")
print(f"- {collected['D']} Christmas decorations")
print(f"- {collected['G']} Gifts")
print(f"- {collected['C']} Cookies")

for row in matrix:
    print(" ".join(row))





