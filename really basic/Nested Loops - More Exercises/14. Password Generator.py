n = int(input())
l = int(input())

for i in range(1 , n +1):
    for i2 in range (1 , n +1):
        for m in range(ord('a'),ord('a')+ l):
            for m2 in range (ord('a'),ord('a')+ l):
                for d in range(1,n +1):
                    if d > i and d > i2:
                        print(f'{i}{i2}{chr(m)}{chr(m2)}{d}', end=" ")