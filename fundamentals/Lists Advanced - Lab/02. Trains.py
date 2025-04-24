wagons_for_the_train = [0] * int(input())

while True:

    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'add':
        wagons_for_the_train[-1] += int(command[1])
    if command[0] == 'insert':
        index = int(command[1])
        wagons_for_the_train[index] += int(command[2])
    if command[0] == 'leave':
        index = int(command[1])
        wagons_for_the_train[index] -= int(command[2])

print(wagons_for_the_train)

