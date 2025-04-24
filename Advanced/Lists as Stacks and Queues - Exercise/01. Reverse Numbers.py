numbers = input().split()
t = []

for i in range(len(numbers)):
    g = numbers.pop()
    t.append(g)

print(' '.join(t))