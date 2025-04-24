size_matrix = int(input())

o = []

for i in range(size_matrix):
    data = [int(x) for x in input().split()]
    o.append(data)

bombs = input().split()

directions = [
         (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)

]

for i in bombs:
    r,c = i.split(',')
    r = int(r)
    c = int(c)
    points = o[r][c]

    if points >0:
        for s,p in directions:
            if 0 <= r + s < len(o) and 0 <= c + p< len(o) and o[r+s][c+p] > 0:
                o[r + s][c + p] -= points

        o[r][c] = 0

counter = 0
total = 0
for e in o:
    for q in e:
        if q > 0:
            total += q
            counter += 1


print(f'Alive cells: {counter}')
print(f'Sum: {total}')

for w in o:
    print(' '.join(map(str,w)))