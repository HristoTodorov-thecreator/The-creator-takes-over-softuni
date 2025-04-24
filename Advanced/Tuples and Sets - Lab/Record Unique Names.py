number_names = int(input())


list_ = []
for s in range(number_names):
    name = input()
    list_.append(name)

to = set(list_)

for t in to:
    print(t)