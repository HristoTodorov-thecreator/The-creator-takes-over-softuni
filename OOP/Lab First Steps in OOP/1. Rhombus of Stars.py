
n = int(input())


def try_(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print(*'*' * i)

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print(*'*' * i)






def rhombus(n):
    try_(n)

rhombus(n)



