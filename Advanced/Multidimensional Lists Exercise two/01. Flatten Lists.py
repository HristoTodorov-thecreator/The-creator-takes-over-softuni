

g = input().split('|')

g = g[::-1]

o = []
for i in g:
    t = i.split()
    o.append(t)

for i in o:
    for s in i :
        print(s,end=' ')
