

first_set = set()

second_set = set()

n = [int(x) for x in input().split()]


for _ in range(n[0]):
    number = input()
    first_set.add(number)







for _ in range(n[1]):
    number_ = input()
    second_set.add(number_)


print('\n'.join(second_set & first_set))
