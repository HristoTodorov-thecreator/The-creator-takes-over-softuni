size = int(input())

matrix= []

bunny_pos = []

best_path = []

best_direction = None

eggs = float('-inf')

best_pos = ''

directions = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right':(0,1),


}

for row in range(size):

    matrix.append(input().split())
    if 'B' in matrix[row]:
        bunny_pos = [row,matrix[row].index('B')]

for direction,position in directions.items():
    row,col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]


    ]
    path = []
    collected = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'X':
            break
        collected += int(matrix[row][col])
        path.append([row,col])
        row += position[0]
        col += position[1]

    if collected >= eggs:
        eggs = collected
        best_path = path
        best_pos = direction
print(best_pos)
print(*best_path,sep='\n')
print(eggs)