list_with_products = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    splitted = command.split()

    if splitted[0] == 'Urgent':
        if splitted[1] not in list_with_products:
            list_with_products.insert(0,splitted[1])

    elif splitted[0] == 'Unnecessary':
        if splitted[1] in list_with_products:
            list_with_products.remove(splitted[1])

    elif splitted[0] == 'Correct':
        if splitted[1] in list_with_products:
            g = list_with_products.index(splitted[1])
            list_with_products[g] = splitted[2]




    elif splitted[0] == 'Rearrange':
        if splitted[1] in list_with_products:
            t = list_with_products.remove(splitted[1])
            list_with_products.append(splitted[1])






print(', '.join(list_with_products))








