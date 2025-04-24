n = int(input())

names = set()

for _ in range(n):
    g = input()
    names.add(g)

for name in names:
    print(name)