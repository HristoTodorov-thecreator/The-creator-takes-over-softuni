number_of_inputs = int(input())


list_for_counter = []
list_for_negative = []


count_of_positeves = 0

sum_of_negatives = 0


for i in range(number_of_inputs):
    number = int(input())
    if number >= 0:
        count_of_positeves += 1
        list_for_counter.append(number)

    else:
        sum_of_negatives += number
        list_for_negative.append(number)


print(list_for_counter)
print(list_for_negative)

print(f'Count of positives: {count_of_positeves}')
print(f'Sum of negatives: {sum_of_negatives}')

