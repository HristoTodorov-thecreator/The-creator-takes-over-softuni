
numbers_given = input()



list = numbers_given.split()

list_with_other_numbers = []
for i in list:
    number = -int(i)
    list_with_other_numbers.append(number)

print(list_with_other_numbers)


