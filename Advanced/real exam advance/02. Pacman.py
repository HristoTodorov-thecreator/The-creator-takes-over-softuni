
size = int(input())

matrix = []

row,col = 0,0

stars = 0

directions = {
    'left':(0,-1),'right':(0,1),'up':(-1,0),'down':(1,0)
}

health = 100
save = False
health_check = False
collected_stars = 0
for row_ in range(size):
    info = list(input())
    matrix.append(info)
    if 'P' in info:
        row,col = row_,info.index('P')
        matrix[row][col] = '-'
    for col_ in range(size):
        if matrix[row_][col_] == '*':
            stars += 1

command = input()

while command != 'end' and health > 0 and collected_stars < stars:
    move = directions[command]

    new_row,new_col = row + move[0],col + move[1]
    if not(0<= new_row <len(matrix) and 0<= new_col <len(matrix)):
        if command == 'left':
            new_col = len(matrix) - 1


        elif command == 'right':
            new_col = 0

        elif command == 'up':
            new_row = len(matrix) - 1

        elif command == 'down':
            new_row = 0


    if matrix[new_row][new_col] == '*':
        matrix[new_row][new_col] = '-'



        collected_stars += 1

    elif matrix[new_row][new_col] == 'G':
        matrix[new_row][new_col] = '-'
        if save:
            save = False

        else:
            health -= 50

    elif matrix[new_row][new_col] == 'F':
        matrix[new_row][new_col] = '-'
        save = True

    row, col = new_row, new_col



    if health <=0:
        print(f'Game over! Pacman last coordinates [{row},{col}]')
        health_check = True

        break


    command = input()
matrix[row][col] = 'P'
if collected_stars == stars:
    print("Pacman wins! All the stars are collected.")
elif collected_stars < stars and not health_check:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if collected_stars < stars:
    print(f'Uncollected stars: {stars-collected_stars}')

for row in matrix:
    print(''.join(row))





