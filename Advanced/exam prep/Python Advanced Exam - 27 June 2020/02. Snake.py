size = int(input())

matrix = []
row,col = 0,0

THE_B = []

for i in range(size):
    info = list(input())
    matrix.append(info)
    if 'S' in info:
        row,col = i,info.index('S')

    for s in range(size):
        if matrix[i][s]== 'B':
            THE_B.append((i,s))



directions = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}


total_food = 0

while total_food < 10:
    command = input()
    coladd,rowadd = directions[command]

    newrow,newcol = row + rowadd, col+ coladd

    if not(0<= newrow <len(matrix) and 0<= newcol <len(matrix)):
        matrix[row][col] = '.'
        print(f'Game over!')

        break
    matrix[row][col] = '.'
    if matrix[newrow][newcol] == '*':
        matrix[newrow][newcol] = 'S'
        total_food += 1

    if (newrow,newcol) in THE_B:
        matrix[newrow][newcol]  = '.'
        THE_B.remove((newrow,newcol))

        newrow,newcol = THE_B[0]
        matrix[newrow][newcol] = 'S'



    row,col = newrow,newcol

if total_food >= 10:
    print(f'You won! You fed the snake.')

print(f'Food eaten: {total_food}')

for row in matrix:
    print(''.join(map(str,row)))



