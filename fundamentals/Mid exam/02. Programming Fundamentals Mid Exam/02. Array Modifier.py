g = list(map(int,input().split()))


while True:
    command = input().split()
    action = command[0]
    if action =='end':
        break

    if action == 'swap':
        indexone = int(command[1])
        indextwo = int(command[2])
        g[indexone] ,g[indextwo] = g[indextwo],g[indexone]

    elif action == 'multiply':
        indexone = int(command[1])
        indextwo = int(command[2])
        g[indexone] *= g[indextwo]

    elif action == 'decrease':
        g = [x-1 for x in g]
print(', '.join(map(str,g)))