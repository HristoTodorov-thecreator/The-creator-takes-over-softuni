
g = input()

list = []
for i in g:
    list.append(i)


number = ''
while list:
    numbert = max(list)
    number += numbert
    list.remove(numbert)

print(number)

