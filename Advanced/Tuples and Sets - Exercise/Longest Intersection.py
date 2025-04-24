n = int(input())
longest = set()
for i in range(n):
    first_range,second_range = input().split('-')
    first_start,first_end = first_range.split(',')
    second_start, second_end = second_range.split(',')

    g = set(range(int(first_start),int(first_end) +1))
    t = set(range(int(second_start),int(second_end )+ 1))

    curr = g & t

    if len(curr) > len(longest):
        longest = curr

print(f'Longest intersection is {list(longest)} with length {len(longest)}')





