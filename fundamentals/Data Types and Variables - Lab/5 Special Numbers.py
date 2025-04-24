n = int(input())

for i in range(1,n+1):
    sum_ = 0
    for s in str(i):
        sum_ += int(s)
    if sum_ == 5 or sum_ == 7 or sum_ == 11:
        print(f'{i} -> True')
    else:
        print((f'{i} -> False'))