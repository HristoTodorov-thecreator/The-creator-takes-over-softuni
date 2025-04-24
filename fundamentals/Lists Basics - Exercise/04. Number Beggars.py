money = input()

number_of_begars = int(input())


g = money.split(', ')

money_as_integer = []
start_index = 0
list_with_begars = []
for money in g:
    money_as_integer.append(int(money))
for current_beggar in range(number_of_begars):
    current_beggar_sum = 0

    for current_index in range(start_index,len(money_as_integer),number_of_begars):

         current_beggar_sum += money_as_integer[current_index]
    list_with_begars.append(current_beggar_sum)
    start_index += 1

print(list_with_begars)



