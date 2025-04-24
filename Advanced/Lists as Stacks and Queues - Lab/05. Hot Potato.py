from collections import deque

kids = deque(input().split())
g = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-g)
    print(f'Removed {kids.popleft()}')




print(f'Last is {kids[-1]}')