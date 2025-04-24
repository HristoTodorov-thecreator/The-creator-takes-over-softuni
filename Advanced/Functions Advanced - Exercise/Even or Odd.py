
def even_odd(*args):
    t = []
    o = []
    final =[]
    for i in args:
        if isinstance(i,int):
            t.append(i)
        else:
            o.append(i)






    if o[0] == 'even':
        for i in t:
            if i % 2 ==0:
                final.append(i)


    else:
        for i in t:
            if i % 2 !=0:
                final.append(i)

    return final

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


