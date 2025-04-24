list_with_Employees = input().split()
factor = int(input())


result = list(map(lambda x: int(x) * factor,list_with_Employees))

sum_ = sum(result)

total = sum_ / len(result)

counter = 0
for i in result:
    if i >= total:
        counter += 1

if counter >= len(result) / 2:
    print(f'Score: {counter}/{len(result)}. Employees are happy!')
else:
    print(f'Score: {counter}/{len(result)}. Employees are not happy!')
