n = int(input())

list_ = []



for i in range(n):
    g = input().split()
    l = [int(m) for m in g]
    list_.append(l)

row_col = input().split()

o = [list(map(int,o.split('-'))) for o in row_col]


destroyed = 0
for row,col in o:
    if list_[row][col] > 0:
        list_[row][col] -= 1
        if list_[row][col] == 0:
            destroyed += 1

print(destroyed)