info = [int(x) for x in input().split()]

for j in range(1,len(info)):

    for i in range(j,0,-1):
        if info[i] < info[i-1]:

            info[i],info[i-1] = info[i-1],info[i]
        else:
            break



print(*info)