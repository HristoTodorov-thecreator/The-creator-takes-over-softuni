n = int(input())


matrix = []
for i in range(n):
    g = [int(x) for x in input().split()]
    matrix.append(g)

total = 0
for s in range(n):
    total += matrix[s][s]


print(total)