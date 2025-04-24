from collections import deque


values_bees = deque([int(x) for x in input().split()])

nectar = [int(x) for x in input().split()]

symbols = deque([x for x in input().split()])

honey = 0
operators = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b if b !=0 else 0
}





while values_bees and nectar:
    first_bee = values_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        the_symb = symbols.popleft()

        honey += abs(operators[the_symb](first_bee, last_nectar))
    else:
        values_bees.appendleft(first_bee)


print(f'Total honey made: {honey}')

if values_bees:
    print(f'Bees left: {", ".join(map(str,values_bees))}')

if nectar:
    print(f'Nectar left: {", ".join(map(str,nectar))}')
