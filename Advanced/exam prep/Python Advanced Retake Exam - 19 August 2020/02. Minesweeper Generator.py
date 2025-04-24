size_mines = int(input())

number_bombs = int(input())

directions = {'left':(0,-1),'right':(0,1),'up':(-1,0),'down':(1,0),
              'first_diag':(-1,-1),'second_diag':(-1,1),
              'third_diag':(1,-1),'forth':(1,1)}

board = []
for _ in range(size_mines):
    second = []
    for _ in range(size_mines):
        second.append('0')
    board.append(second)


for _ in range(number_bombs):
    row,col = input().replace('(','').replace(')','').split(', ')
    row = int(row)
    col = int(col)
    board[row][col] = '*'


for rowo in range(size_mines):

    for colo in range(size_mines):



        if board[rowo][colo] == '*':
            continue

        total = 0

        for rowtwo,coltwo in directions.values():
            new_row,new_col = rowo + rowtwo,colo +coltwo
            if not (0 <= new_row < len(board) and 0 <= new_col < len(board)):
                continue

            if board[new_row][new_col] == '*':
                total += 1


        board[rowo][colo] = str(total)

for s in range(size_mines):
    print(*board[s])




