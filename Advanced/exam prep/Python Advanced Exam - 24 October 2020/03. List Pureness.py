def best_list_pureness(args,k):
    best = float('-inf')
    best_rot = 0

    for rotation in range(k+1):
        pureness = sum(args[i] * i for i in range(len(args)))

        if pureness > best:
            best = pureness
            best_rot = rotation

        args.insert(0,args.pop())

    return f'Best pureness {best} after {best_rot} rotations'






test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)