def s(mat, bunnies):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                mat[new_row][new_col] = 'B'
                new_bunnies.add((new_row, new_col))
    return mat, bunnies.union(new_bunnies)


rows, cols = [int(x) for x in input().split()]

matrix = []

has_won = False
has_lost = False
p_row, p_col = 0, 0

bunnies = set()

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'P':
            p_row = row
            p_col = col
        elif matrix[row][col] == 'B':
            bunnies.add((row, col))

commands = list(input())
moves = {
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c),
    'L': lambda r, c: (r, c - 1),
    'R': lambda r, c: (r, c + 1)
}

for command in commands:
    new_p_row, new_p_col = moves[command](p_row, p_col)
    matrix, bunnies = s(matrix, bunnies)

    if (p_row, p_col) not in bunnies:
        matrix[p_row][p_col] = '.'

    if new_p_row < 0 or new_p_row >= rows or new_p_col < 0 or new_p_col >= cols:
        has_won = True
        break

    if matrix[new_p_row][new_p_col] == 'B':
        has_lost = True
        p_row, p_col = new_p_row, new_p_col
        break

    p_row, p_col = new_p_row, new_p_col

for row in matrix:
    print(''.join(row))

if has_won:
    print(f'won: {p_row} {p_col}')
elif has_lost:
    print(f'dead: {p_row} {p_col}')