numbers = input().split()

thenumber = int(input()) # count of number to remove

list_with_int = []

for value in numbers:
    list_with_int.append(int(value))

for i in range(thenumber):
    list_with_int.remove(min(list_with_int))


string_list = [str(num) for num in list_with_int]

print(', '.join(string_list))