numbers_given = input().split()

the_new_list = []


for i in numbers_given:
    g = abs(float(i))
    the_new_list.append(g)

print(the_new_list)