from sys import maxsize

numbers = int(input())

totalbig = - maxsize
totalsmall = maxsize

for _ in range(numbers):
    num_ = int(input())
    if num_ < totalsmall:
        totalsmall = num_

    if num_ > totalbig:
        totalbig = num_


y = 'Max number:'
z = 'Min number:'


print(f'{y} {totalbig}')
print(f'{z} {totalsmall}')


