a1 = int(input())
a2 = int(input())
n = int(input())

for i in range(a1 , a2):
    char = chr(i)
    for i2 in range(1 ,n):
        for i3 in range(1,n // 2):
            i4 = i
            if i % 2 != 0 and (i2 + i3 + i4) % 2 != 0:
                print(f'{char}-{i2}{i3}{i4}')
