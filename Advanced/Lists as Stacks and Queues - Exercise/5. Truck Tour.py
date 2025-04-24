from collections import deque
pumps = int(input())

allpumps = deque()



for i in range(pumps):
    fuel,kms = input().split()
    allpumps.append([int(fuel),int(kms)])


stop = 0
start = 0

while stop < pumps:
    fuel = 0
    for i in range(pumps):
        fuel += allpumps[i][0]
        distance = allpumps[i][1]
        if fuel < distance:
            allpumps.rotate(-1)
            start += 1
            stop = 0
            break

        else:
            fuel -= distance
            stop += 1


print(start)