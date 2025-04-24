
def grocery_store(**kwargs):
    r = sorted(kwargs.items(),key=lambda x: (-x[1],-len(x[0]),x[0]))

    result = []


    for p,q in r:
        result.append(f'{p}: {q}')

    return '\n'.join(result)




print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))