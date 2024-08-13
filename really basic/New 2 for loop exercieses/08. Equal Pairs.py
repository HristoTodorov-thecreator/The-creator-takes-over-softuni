ranges = int(input())


firstdif = 0
secdiff = 0
thirddiff = 0


sum_ = 0
for i in range(ranges):
    sum_ = int(input()) + int(input())

    if i == 0:
        firstdif = sum_
    if sum_ != firstdif:
        secdiff = abs(sum_ - firstdif)
        firstdif = sum_
    if secdiff > thirddiff:
        thirddiff = secdiff

if thirddiff == 0:
    print(f"Yes, value={sum_}")
else:
    print(f"No, maxdiff={thirddiff}")







