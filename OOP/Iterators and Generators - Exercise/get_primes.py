
t = [2,3,5,7,11]
def get_primes(g):
    result = []
    for i in g:
        if i < 2:
            continue
        for g in range(2,i):
            if i % g == 0:
                break
        else:
            yield i

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
