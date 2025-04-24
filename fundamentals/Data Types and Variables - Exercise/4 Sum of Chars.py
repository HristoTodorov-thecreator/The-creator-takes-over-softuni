number_of_lines = int(input())


sum_ = 0
for i in range(number_of_lines):
    letter = input()
    sum_ += ord(letter)
print(f'The sum equals: {sum_}')