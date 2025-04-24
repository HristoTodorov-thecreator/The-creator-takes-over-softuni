n = int(input())

matrix = []
data = []
for m in range(n):
    the = input().split(', ')
    data.append(the)
for s in data:
    list_ = []
    for n in s:
        n = int(n)
        if n % 2 == 0:
            list_.append(n)
    matrix.append(list_)

print(matrix)





