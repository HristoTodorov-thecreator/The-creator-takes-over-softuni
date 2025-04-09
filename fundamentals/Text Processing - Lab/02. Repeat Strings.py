g = input().split()


total = ''
for i in range(len(g)):
    lentgh = len(g[i])
    total += g[i] * lentgh

print(total)