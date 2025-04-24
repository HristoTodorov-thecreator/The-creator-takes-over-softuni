factor = int(input())
count = int(input())


result = []


for i in range(1,count +1):
    number = factor * i
    result.append(number)

print(result)