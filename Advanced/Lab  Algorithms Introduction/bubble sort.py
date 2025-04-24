info = [int(x) for x in input().split()]

is_sorted = False

sorted_elements = 0

while not is_sorted:
    is_sorted = True
    for j in range(1,len(info) - sorted_elements):
        i = j-1
        if info[i] > info[j]:
            is_sorted = False
            info[i],info[j] = info[j],info[i]
    sorted_elements += 1

print(*info)