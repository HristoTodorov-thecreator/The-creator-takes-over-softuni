result = 0
n = int(input())
for i in range (1,n+1):
    for t in range (1 ,   i + 1):
        result += 1
        print(result, end=' ')
        if result == n:
            exit()
    print()
