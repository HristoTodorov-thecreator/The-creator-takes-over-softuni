


number = int(input())
g = str(number)

l = len(g)

mylist = []




for i in g:
   n = int(i)
   mylist.append(n)

number2 = 0

for m in range(l):
    maxdigit_ = 0

    maxdigit_ = max(mylist)
    str(maxdigit_)
    number2 += maxdigit_

    mylist.remove(max(mylist))


