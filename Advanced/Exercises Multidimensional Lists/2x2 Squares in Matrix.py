g = input().split()

row = int(g[0])
col = int(g[1])

matrix = [[x for x in input().split(' ')]for i in range(row)]

total = 0
for i in range(row -1):

    for s in range(col -1):




        if matrix[i][s] == matrix[i][s+1] and matrix[i][s] ==  matrix[i+1][s] and matrix[i][s] == matrix[i+1][s+1]:
            total += 1



print(total)
