targets = [int(x) for x in input().split()]

def shoot(index,power):
    if 0 <= index < len(targets):
        targets[index] -= power

        if targets[index] <= 0:
            del targets[index]


def add(index,power):
    if 0 <= index < len(targets):
        targets.insert(index,power)

    else:
        print(f"Invalid placement!")

def strike(index,radius):
    start = index - radius
    end = index + radius
    if end < len(targets) and start >= 0:

        del targets[start:end + 1]
    else:
        print(f"Strike missed!")


while True:
    command = input()
    if command == 'End':
        break
    splitted = command.split()
    action = splitted[0]

    if action == 'Shoot':
        index = int(splitted[1])
        power = int(splitted[2])
        shoot(index,power)
    if action == 'Add':
        index = int(splitted[1])
        power = int(splitted[2])
        add(index,power)

    if action == 'Strike':
        index = int(splitted[1])
        radius = int(splitted[2])
        strike(index,radius)


print('|'.join(map(str,targets)))