first_input = input().split(', ')
second_input = input().split(', ')

the_new_list = []


for i in first_input:
    for t in second_input:
        if i in t:
            the_new_list.append(i)
            break

print(the_new_list)
