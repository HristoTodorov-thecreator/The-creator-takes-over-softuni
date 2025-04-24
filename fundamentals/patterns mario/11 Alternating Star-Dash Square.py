n = int(input())

for i in range(n):
    for s in range(n):
        if (i + s ) % 2 ==0:
            print('*',end='')
        else:
            print('-',end='')
    print()