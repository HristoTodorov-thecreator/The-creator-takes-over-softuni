
def even_odd_filter(**kwargs):
    for key,numbers in kwargs.items():
        if key == 'even':

            kwargs[key] = [x for x in numbers if x % 2 ==0]
        else:
            kwargs[key] = [x for x in numbers if x % 2 != 0]

    return dict(sorted(kwargs.items(),key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))