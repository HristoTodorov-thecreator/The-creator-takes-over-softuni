people_waiting = int(input())

lifts = list(map(int,input().split()))

for i in range(len(lifts)):
    space = 4 - lifts[i]

    if people_waiting >= space:
        lifts[i] += space
        people_waiting -= space
    else:
        lifts[i] += people_waiting
        people_waiting = 0
    if people_waiting == 0:
        break


g = [str(t) for t in lifts]

if people_waiting == 0 and any(the < 4 for the in lifts):
    print(f"The lift has empty spots!")
    print(f' '.join(g))
elif people_waiting >0 and all(them == 4 for them in lifts):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(f' '.join(g))
else:
    print(f' '.join(g))


