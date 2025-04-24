


given_numbers = input().split()


new_list = []
for i in given_numbers:
    t = float(i)
    round_number = round(t)
    new_list.append(round_number)

print(new_list)
