journal = input().split(', ')

while True:
    command = input()

    if command == 'Craft!':
        break

    split = command.split(' - ')
    if split[0] == 'Collect':
        item = split[1]
        if item not in journal:
            journal.append(item)
    if split[0] == 'Drop':
        item = split[1]
        if item in journal:
            journal.remove(item)

    if split[0] == 'Combine Items':
        items = split[1]
        splitedtwo = items.split(':')
        firsti = splitedtwo[0]
        secondi = splitedtwo[1]


        if splitedtwo[0] in journal:
            g = journal.index(firsti)
            journal.insert(g+1,secondi)

    if split[0] == 'Renew':
        item = split[1]
        if item in journal:
            ind = journal.index(item)
            t = journal.pop(ind)
            journal.append(t)

print(', '.join(s for s in journal))