g = input().split(', ')
g = [int(x) for x in g]
matrix = []

for i in range(g[0]):
    l = [int(x) for x in input().split()]
    matrix.append(l)


for s in range(g[1]):
    col = 0

    for t in range(g[0]):
        col += matrix[t][s]


    print(col)




