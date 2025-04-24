from collections import deque

robots = input().split(';')
robots_list = []

for g in robots:
    robot_name,time = g.split('-')
    time = int(time)

    robots_list.append({'name': robot_name,'the_time':time,'p': 0})


hours,minutes,seconds = [int(x) for x in input().split(':')]

products = deque()

start = hours * 3600 + minutes * 60 + seconds
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)
while products:
    current = products.popleft()
    start += 1

    is_taken = False

    for robot in robots_list:
        if robot['p'] <= start:
            robot['p'] = start + robot['the_time']
            h = start // 3600
            m = (start % 3600) // 60
            s = (start % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break


    if not is_taken:
        products.append(current)
