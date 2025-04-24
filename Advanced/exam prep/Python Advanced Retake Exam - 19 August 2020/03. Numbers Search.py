

def numbers_searching(*args):

    set_nums = set(args)
    maxnum = max(args)
    minnum = min(args)
    list_ = []
    for i in range(minnum,maxnum+1):
        list_.append(i)
    for s in set_nums:
        if s in list_:
            list_.remove(s)

    list_ = [list_[-1]]
    duplicate = list()
    not_duplicate = []

    for n in args:
        if n not in not_duplicate:
            not_duplicate.append(n)
        else:
            if n in duplicate:
                continue
            else:
                duplicate.append(n)

    list_.append(sorted(duplicate))

    return list_




print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))



print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))