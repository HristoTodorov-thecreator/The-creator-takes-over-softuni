
matrix = []
white_row,white_col = 0,0
black_row,black_col = 0,0

def check_white(white_row, white_col):
    for col_diff in (-1, 1):
        new_row = white_row - 1
        new_col = white_col + col_diff
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if matrix[new_row][new_col] == 'b':
                return True, new_row, new_col
    return False, white_row, white_col

def check_black(black_row, black_col):
    for col_diff in (-1, 1):
        new_row = black_row + 1
        new_col = black_col + col_diff
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if matrix[new_row][new_col] == 'w':
                return True, new_row, new_col
    return False, black_row, black_col





def get_chess_position(row, col):
    position_row = {
        0: "8",
        1: "7",
        2: "6",
        3: "5",
        4: "4",
        5: "3",
        6: "2",
        7: "1",
    }
    positions_col = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
    }
    pos_one,pos_two = position_row[row],positions_col[col]
    result = f'{pos_two}{pos_one}'
    return result

for i in range(8):
    data = input().split()

    matrix.append(data)
    for s in range(8):
        if matrix[i][s] == 'w':
            white_row,white_col = i,s

        elif matrix[i][s] == 'b':
            black_row,black_col = i,s

while True:
    if white_row == 0:
        t = get_chess_position(white_row, white_col)
        print(f"Game over! White pawn is promoted to a queen at {t}.")
        break

    found, white_row, white_col = check_white(white_row, white_col)
    if found:
        t = get_chess_position(white_row, white_col)
        print(f"Game over! White win, capture on {t}.")
        break



    matrix[white_row][white_col] = '-'
    white_row -= 1
    matrix[white_row][white_col] = 'w'

    if black_row == 7:
        t = get_chess_position(black_row, black_col)
        print(f"Game over! Black pawn is promoted to a queen at {t}.")
        break

    found, black_row, black_col = check_black(black_row, black_col)
    if found:
        t = get_chess_position(black_row, black_col)
        print(f"Game over! Black win, capture on {t}.")
        break

    matrix[black_row][black_col] = '-'
    black_row += 1
    matrix[black_row][black_col] = 'b'

