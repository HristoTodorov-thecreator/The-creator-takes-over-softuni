MINIMUM_FOR_PRICE = 100

matrix = []
for row in range(6):
    info = input().split()
    matrix.append(info)


total = 0
hitted = set()

def check(total):
    if 100 <= total <= 199:
        return 'Football'
    elif 200<= total <= 299:
        return 'Teddy Bear'
    elif total >= 300:
        return 'Lego Construction Set'

    return None



for hit in range(3):
    row,col = input().replace('(','').replace(')','').split(', ')
    row = int(row)
    col = int(col)

    if 0<= row < len(matrix) and 0<=col <len(matrix):
        if matrix[row][col] == 'B' and (row,col) not in hitted:
            hitted.add((row,col))
            for i in range(6):
                if matrix[i][col].isdigit():
                    total += int(matrix[i][col])

if total < 100:
    print(f'Sorry! You need {MINIMUM_FOR_PRICE - total} points more to win a prize.')
else:
    p = check(total)
    print(f"Good job! You scored {total} points, and you've won {p}.")





