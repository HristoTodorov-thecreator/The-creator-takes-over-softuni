
word = input()

list_with_numbers = []



counter = 0
for i in word:


    if i.isupper():
        list_with_numbers.append(counter)

    counter += 1

print(list_with_numbers)