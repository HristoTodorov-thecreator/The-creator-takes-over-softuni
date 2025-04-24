
from itertools import permutations
def possible_permutations(g):
    for i in permutations(g):
        yield list(i)

[print(n) for n in possible_permutations([1, 2, 3])]