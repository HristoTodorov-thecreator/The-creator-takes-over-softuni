n = int(input())


matrix = [[int(x) for x in input().split()]for i in range(n)]

first = [[matrix[i][i]]for i in range(n)]

second = [[matrix[i][-1 - i]]for i in range(n)]

_total = 0
_totaltwo = 0
for s in first:
    for t in s:
        _total += t

for m in second:
    for n in m:
        _totaltwo += n


print(abs(_total - _totaltwo))


