n = int(input())

for i in range(1,n+1):
    for _ in range(n - i):
        print(' ',end='')

    for x in range(1,i+1):
        print(x,end='')

    for x in range(i - 1, 0, -1):
        print(x, end='')
    print()

for i in range(n-1,0,-1):
    for _ in range(n - i):
        print(' ',end='')
    for x in range (1,i + 1):
        print(x,end='')

    for x in range (i - 1,0,-1):
        print(x,end='')
    print()