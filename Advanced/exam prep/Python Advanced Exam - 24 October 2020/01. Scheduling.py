

jobs = [int(x) for x in input().split(", ")]

the_index = int(input())

print(sum([number for number in jobs if number <= jobs[the_index]]))
