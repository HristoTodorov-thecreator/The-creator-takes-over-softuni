n = int(input())

for i in range (1, n+1):
    for j in range(0,i):
        print('*',end= '')
    print()
for s in range(n - 1,0,-1):
    for k in range(0,s):
        print('*',end='')
    print()