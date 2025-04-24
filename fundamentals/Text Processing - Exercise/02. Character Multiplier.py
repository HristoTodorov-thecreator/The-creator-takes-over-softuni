first, second = input().split()


min_length = min(len(first), len(second))
total_sum = 0


for i in range(min_length):
    total_sum += ord(first[i]) * ord(second[i])


for i in range(min_length, len(first)):
    total_sum += ord(first[i])

for i in range(min_length, len(second)):
    total_sum += ord(second[i])


print(total_sum)