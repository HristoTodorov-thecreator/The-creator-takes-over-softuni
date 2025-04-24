number_list = []
non_number_list = []

text = input()

skip_list = []
take_list = []


for letter in text:
    if letter.isdigit():
        number_list.append(int(letter))
    else:
        non_number_list.append(letter)

for one_number in range(len(number_list)):
    curr_number = number_list[one_number]
    if one_number % 2 == 0:
        take_list.append(curr_number)


    else:
        skip_list.append(curr_number)


result = ''

for item in range(len(skip_list)):
    take_number = take_list[item]
    skip_number = skip_list[item]
    result += ''.join(non_number_list[:take_number])

    non_number_list = non_number_list[take_number + skip_number:]


print(result)



