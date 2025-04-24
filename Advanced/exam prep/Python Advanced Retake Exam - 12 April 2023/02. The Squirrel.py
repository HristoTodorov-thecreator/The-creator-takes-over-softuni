
hazelnuts = 0
n = int(input())

moves = input().split(', ')

row,col = 0,0

matrix = []

directions = {
    'left':(0,-1),'right':(0,1),'up':(-1,0),'down':(1,0)
}


for i in range(n):
    info = list(input())
    matrix.append(info)
    if 's' in info:
        row,col = i,info.index('s')

trap_or_out = False

for move in moves:
    the_move = directions[move]
    new_row,new_col = row + the_move[0] ,col + the_move[1]

    if 0<= new_row <len(matrix) and 0<= new_col <len(matrix):
        row,col = new_row,new_col
        if matrix[new_row][new_col] == 'h':
            hazelnuts += 1
            matrix[new_row][new_col] = '*'
        if hazelnuts >= 3 :
            print(f'Good job! You have collected all hazelnuts!')
            break
        if matrix[new_row][new_col] == 't':
            print(f'Unfortunately, the squirrel stepped on a trap...')
            trap_or_out = True
            break
    else:
        print(f'The squirrel is out of the field.')
        trap_or_out = True
        break

if hazelnuts <3 and not trap_or_out:
    print(f'There are more hazelnuts to collect.')



print(f'Hazelnuts collected: {hazelnuts}')







