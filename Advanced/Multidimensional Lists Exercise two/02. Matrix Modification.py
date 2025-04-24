n_matrix_rows = int(input())

o = []
for i in range(n_matrix_rows):
    data = [int(x) for x in input().split()]
    o.append(data)


def check(r,c,n):
    return 0 <= r < n and 0 <= c < n


commands = input()

while commands != 'END':

    g = commands.split()
    thecommand = g[0]
    r = int(g[1])
    c = int(g[2])
    value = int(g[3])

    if thecommand == 'Add':
        if check(r,c,n_matrix_rows):
            o[r][c] += value
        else:
            print(f'Invalid coordinates')



    if thecommand == 'Subtract':
        if check(r,c,n_matrix_rows):
            o[r][c] -= value
        else:
            print(f'Invalid coordinates')

    commands = input()

for i in o:
    print(*i)


