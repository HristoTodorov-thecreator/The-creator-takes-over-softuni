
directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}

rows = 8

row, col = 0, 0
board = []
for i in range(rows):
    data = input().split()
    if 'K' in data:
        row, col = i, data.index('K')

    board.append(data)




queens_pos = []

def check(row,col,board):
    return 0<= row <len(board) and 0<= col < len(board)

def movement(new_row,new_col,move):
    return new_row + directions[move][0] , new_col + directions[move][1]

for move in directions:
    new_row,new_col = row,col

    for st in range(rows):
        new_row,new_col = movement(new_row,new_col,move)
        if check(new_row,new_col,board):
            if board[new_row][new_col] == 'Q':
                queens_pos.append([new_row,new_col])
                break

        else:
            break

if queens_pos:
    [print(row) for row in queens_pos]
else:
    print("The king is safe!")




