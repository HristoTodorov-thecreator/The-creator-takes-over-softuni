nums = tuple(float(x) for x in input().split())

d = {}


for l in nums:
    if l not in d:
        number = nums.count(l)
        d[l] = {'count':number}

for n in d:
    print(f"{n} - {d[n]['count']} times")