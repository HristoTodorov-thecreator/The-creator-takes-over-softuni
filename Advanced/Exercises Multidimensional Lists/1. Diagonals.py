n = int(input())

matrix = [[int(x) for x in input().split(', ')]for i in range(n)]

first = [[matrix[i][i]]for i in range(n)]

second = [[matrix[i][-1 - i]]for i in range(n)]


print(f'Primary diagonal: {", ".join(str(x[0]) for x in first)}. Sum: {sum(x[0] for x in first)}')

print(f'Secondary diagonal: {", ".join(str(x[0]) for x in second)}. Sum: {sum(x[0] for x in second)}')