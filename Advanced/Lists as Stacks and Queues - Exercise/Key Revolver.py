from collections import deque

price_for_bullet = int(input())

barrel_size = int(input())

bullets = [int(x) for x in input().split()]

locks = deque([int(s) for s in input().split()])

value_ = int(input())



bullets_used = 0
current_size = barrel_size
while bullets and locks:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()


    if current_lock >= current_bullet:
        print(f'Bang!')
        bullets_used += 1
    else:
        locks.appendleft(current_lock)
        bullets_used += 1
        print(f'Ping!')

    current_size -= 1
    if current_size == 0 and bullets:
        print(f'Reloading!')
        current_size = barrel_size



if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${value_ - (bullets_used * price_for_bullet)}')
