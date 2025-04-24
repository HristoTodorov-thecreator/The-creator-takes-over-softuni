numbers = list(map(int,input().split()))
targets = int(input())

for i in range(len(numbers)):
    if numbers[i] == '':
        continue
    for j in range(i+1 ,len(numbers)):
        if numbers[j] == '':
            continue
        if numbers[i] + numbers[j] == targets:
            print(f'{numbers[i]} + {numbers[j]} = {targets}')
            numbers[i] = ''
            numbers[j] = ''
            break


