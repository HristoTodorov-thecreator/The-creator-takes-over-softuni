n = int(input())


matrix=[]
for _ in range(n):
    g = list(input())
    matrix.append(g)





searched = input()

for s in range(len(matrix)):

    for t in range(len(matrix[s])):
        if matrix[s][t] == searched:
            print(f'({s}, {t})')
            exit()


print(f'{searched} does not occur in the matrix')