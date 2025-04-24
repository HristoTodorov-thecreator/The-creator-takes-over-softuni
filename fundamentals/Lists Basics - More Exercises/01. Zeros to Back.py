numbers = input().split(', ')

numbers = [int(m) for m in numbers]
zeros = [num for num in numbers if num != 0]
nums = [numt for numt in numbers if numt == 0]

alll = zeros + nums

print(alll)