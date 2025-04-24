rows,cols = map(int,input().split())


matrix = [[int(x) for x in input().split()]for i in range(rows)]

max_sum = -float('inf')

max_row = 0
max_col = 0


for i in range(rows - 2):
    for s in range(cols - 2):
        current_sum = 0
        for r in range(i,i+3):
            for c in range(s,s+3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = i
            max_col = s

print(f'Sum = {max_sum}')

for r in range(max_row, max_row + 3):
    print(*matrix[r][max_col:max_col + 3])