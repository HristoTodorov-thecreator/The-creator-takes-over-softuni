N = int(input())

for i in range(1,10):
    for z in range(1,10):
        for k in range(1,10):
            for m in range(1,10):
                if i + z == k + m:
                    if N % (i + z) == 0:
                         print(f'{i}{z}{k}{m}', end= ' ')