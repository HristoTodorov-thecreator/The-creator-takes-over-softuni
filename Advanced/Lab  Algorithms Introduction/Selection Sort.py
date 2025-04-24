info = [int(x) for x in input().split()]

n = len(info)

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if info[j] < info[min_index]:
            min_index = j

    info[i],info[min_index] = info[min_index],info[i]

print(*info)