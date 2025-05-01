
n = int(input())

collected_stars = 2
matrix = []
row,col = 0,0


for i in range(n):
    data = input().split()
    matrix.append(data)
    for s in range(n):
        if matrix[i][s] == 'P':
            row,col = i,s
initial_position_marked = False
while True:

    if collected_stars >= 10:
        break
    if collected_stars <= 0 :
        break
    command = input()
    if not initial_position_marked:
        matrix[row][col] = '.'
        initial_position_marked = True
    new_row,new_col = row,col

    if command == 'left':
        new_col -= 1
    elif command == 'right':
        new_col += 1
    elif command == 'up':
        new_row -=1
    elif command == 'down':
        new_row += 1

    if not(0 <= new_row < n and 0 <= new_col < n):
        new_row,new_col = 0,0

    if matrix[new_row][new_col] == '#':
        collected_stars -= 1
        continue


    if matrix[new_row][new_col] == '*':
        collected_stars += 1

    matrix[new_row][new_col] = '.'
    row, col = new_row, new_col

if collected_stars == 10:
    print(f"You won! You have collected 10 stars.")

else:
    print(f"Game over! You are out of any stars.")

print(f'Your final position is [{row}, {col}]')
matrix[row][col] = 'P'

for i in matrix:
    print(*i)










