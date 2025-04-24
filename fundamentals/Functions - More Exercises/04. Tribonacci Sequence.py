n= int(input())


list_ = [1, 0, 0]

def t(n):
    for i in range(n):
        next = sum(list_)
        print(next, end=" ")
        list_.append(next)
        list_.pop(0)

t(n)