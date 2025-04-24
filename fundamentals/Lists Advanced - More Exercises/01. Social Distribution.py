numbers = list(map(int,input().split(', ')))

min_wealth = int(input())

if sum(numbers) < min_wealth * len(numbers):
    print(f'No equal distribution possible')
else:
    for i in range(len(numbers)):
        if numbers[i] < min_wealth:
            max_ind = numbers.index(max(numbers))

            diff = min_wealth - numbers[i]
            numbers[max_ind] -= diff
            numbers[i] += diff

    print(numbers)


