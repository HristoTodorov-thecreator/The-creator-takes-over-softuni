values_one = [int(x) for x in input().split()]
values_two = [int(x) for x in input().split()]
values_one = set(values_one)
values_two = set(values_two)

n = int(input())

for i in range(n):
    command = input()
    if 'Add First' in command:
        command = command.replace('Add First','')
        command = command.split()
        for s in command:
            values_one.add(int(s))
    if 'Add Second' in command:
        command = command.replace('Add Second', '')
        command = command.split()
        for o in command:
            values_two.add(int(o))

    if 'Remove First' in command:
        command = command.replace('Remove First', '')
        command = command.split()

        for t in command:
            if int(t) in values_one:
                values_one.remove(int(t))
    if 'Remove Second' in command:
        command = command.replace('Remove Second', '')
        command = command.split()

        for q in command:
            if int(q) in values_two:
                values_two.remove(int(q))

    if 'Check Subset' in command:
        print(values_one.issubset(values_two) or values_two.issubset(values_one))


print(', '.join(map(str,sorted(values_one))))
print(', '.join(map(str,sorted(values_two))))