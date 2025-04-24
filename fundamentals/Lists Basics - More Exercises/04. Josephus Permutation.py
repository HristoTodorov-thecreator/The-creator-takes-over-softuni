list_with_numbers = input().split()
number = int(input())
pos = number - 1
index = 0
the_new_list = []

while list_with_numbers:
    index = (pos + index) % len(list_with_numbers)

    the_new_list.append(list_with_numbers.pop(index))

print(f"[{','.join(the_new_list)}]")