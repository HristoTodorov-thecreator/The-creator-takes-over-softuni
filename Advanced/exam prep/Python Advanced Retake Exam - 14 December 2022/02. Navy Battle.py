size = int(input())
matrix= []


directions = {
    'left':(0,-1),'right':(0,1),'up':(-1,0),'down':(1,0)
}
lives = 3
for_win = 3

row,col = 0,0
for i in range(size):
    info = list(input())
    matrix.append(info)
    if 'S' in info:
        row,col = i,info.index('S')
matrix[row][col] = '-'

while True:
    command = input()

    move = directions[command]
    new_row,new_col = row + move[0],col +move[1]


    if 0<=new_row <len(matrix) and 0<= new_col < len(matrix):
        row,col = new_row,new_col
        if matrix[new_row][new_col] == '*':
            matrix[new_row][new_col] = '-'
            lives -= 1
            if lives == 0:
                print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
                break

        elif matrix[new_row][new_col] == 'C':
            matrix[new_row][new_col] = '-'
            for_win -= 1
            if for_win == 0:
                print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
                break
matrix[row][col] = 'S'
for row in matrix:
    print(''.join(row))





