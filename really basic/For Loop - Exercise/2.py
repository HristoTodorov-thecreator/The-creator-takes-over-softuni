from sys import maxsize

maxnumber = - maxsize
total = 0

number = int(input())

for i in range(number):
    g = int(input())
    total = total + g

    if g > maxnumber:
        maxnumber = g

halfnum = total - maxnumber

if maxnumber == halfnum:
    print(f'Yes\nSum = {halfnum}')
else:
    print(f'No\nDiff = {abs(maxnumber - halfnum)}')









