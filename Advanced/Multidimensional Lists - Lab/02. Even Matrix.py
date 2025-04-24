n = int(input())

matrix = []
for i in range(n):
    data = [int(x) for x in input().split(', ')]
    datatwo = [x for x in data if x % 2 ==0]
    matrix.append(datatwo)


print(matrix)
