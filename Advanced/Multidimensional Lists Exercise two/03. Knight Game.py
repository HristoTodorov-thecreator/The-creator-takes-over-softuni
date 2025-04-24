size = int(input())


matrix = [list(input()) for _ in range(size)]


moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1))


removed = 0

while True:
    max_attacks = 0
    knight_with_most_attacks  = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in moves:
                    pos_row = row + pos[0]

                    pos_col = col + pos[1]
                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [row,col]

    if knight_with_most_attacks:
        r, c = knight_with_most_attacks
        matrix[r][c] = '0'
        removed += 1
    else:
        break

print(removed)


