name = sorted(input())

t = []
o = []

counter = 0

for i in name:
    if i not in t:
        t.append(i)

        o.append(1)


    else:
        m = t.index(i)
        o[m] += 1
for q in range(len(t)):
    print(f'{t[q]}: {o[q]} time/s')




