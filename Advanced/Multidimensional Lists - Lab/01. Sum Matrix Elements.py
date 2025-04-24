
matrix =[]

total = 0
rows,cols = input().split(', ')

for row in range(int(rows)):
    data = [int(x) for x in input().split(', ')]
    total += sum(data)
    matrix.append(data)

print(total)
print(matrix)

