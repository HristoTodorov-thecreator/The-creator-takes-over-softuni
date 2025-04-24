rows_count = int(input())

matrix = []

for _ in range(rows_count):
    data = input().split(', ')
    for s in data:
        matrix.append(int(s))

print(matrix)