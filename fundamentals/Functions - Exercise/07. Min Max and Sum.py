numbers = input().split()
list_ = []
for i in numbers:
    list_.append(int(i))





def min_():
    return min(list_)
def max_():
    return max(list_)
def sum_():
    return sum(list_)

first = min_()
second = max_()
third = sum_()

print(f'The minimum number is {first}')
print(f'The maximum number is {second}')
print(f'The sum number is: {third}')
