firstnum = int(input())
secnum = int(input())


for i in range (firstnum,secnum + 1):
    for z in range (firstnum,secnum + 1):
        for m in range(firstnum ,secnum + 1):
            for l in range(firstnum , secnum + 1):
                if  i > l:
                    if (z + m) % 2 == 0:
                        if i % 2 == 0:
                            if l % 2 != 0:
                                print(f'{i}{z}{m}{l}',end=' ')
                        elif i % 2 !=0:
                            if l % 2 == 0:
                                print(f'{i}{z}{m}{l}',end=' ')