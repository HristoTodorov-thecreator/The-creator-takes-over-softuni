def for_thenumbers(num):
    return num % 2 ==0


numbers = input()

list_ = [int(i) for i in numbers.split()]

even = filter(for_thenumbers,list_)
listt  = list(even)
print(listt)
