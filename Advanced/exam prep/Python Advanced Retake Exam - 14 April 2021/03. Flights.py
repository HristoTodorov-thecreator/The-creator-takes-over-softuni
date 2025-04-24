def flights(*args):

    o = {}
    for i in range(0,len(args)+1,2):
        if args[i] == 'Finish':
            break
        else:
            if args[i] not in o:
                o[args[i]] = 0
            o[args[i]] += int(args[i + 1])

    return o



print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))