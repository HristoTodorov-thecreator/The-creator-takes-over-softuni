numbers = int(input())

leftsum = 0
rightsum  = 0



for _ in range(numbers):
    g = int(input())
    rightsum = rightsum + g

for _ in range(numbers):
    g = int(input())
    leftsum = leftsum + g

if leftsum == rightsum:
    print(f'Yes, sum = {leftsum}')
elif leftsum != rightsum:
    m = abs(leftsum - rightsum)
    print(f'No, diff = {m}')
