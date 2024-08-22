
firn = int(input())
secn = int(input())
thirdn = int(input())




for i in range(2,firn + 1,2):
    for s in range (2,secn + 1):
        if s == 2 or s == 3 or s == 5 or s == 7:
           for m in range (2,thirdn + 1,2):
            print(f'{i} {s} {m}')
