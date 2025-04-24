numbers = input().split()
summ = list(map(int,numbers))

sum_numbers = sum(summ)


avarage = sum_numbers / len(numbers)

new_list_with_numbers_greater_than_average = []


for i in summ:
    if i > avarage:
        new_list_with_numbers_greater_than_average.append(i)

t = sorted(new_list_with_numbers_greater_than_average,reverse=True)
top_5_list = t[:5]

if top_5_list:
    print(' '.join(map(str, top_5_list)))
else:
    print(f'No')