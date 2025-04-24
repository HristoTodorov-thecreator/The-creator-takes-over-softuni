coll = set([int(x) for x in input().split(', ')])

n = int(input())

sets = [set(map(int,input().split(', ')))for i in range(n)]

collected_sets = []

while coll:
    best_set = max(sets,key=lambda s: len(s & coll))
    collected_sets.append(best_set)
    coll -= best_set
    sets.remove(best_set)

print(f'Sets to take ({len(collected_sets)}):')

for s in collected_sets:
    if len(s) == 1:

        print(f"{{ {str(*s)} }}")
    else:
        print(f"{{ {', '.join(map(str,s))} }}")