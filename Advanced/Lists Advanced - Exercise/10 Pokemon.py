numbers = [int(x) for x in input().split()]

removed_sum = 0


while numbers:
    index_ = input()
    removed = 0
    if int(index_) <0 :
        removed = numbers[0]
        numbers[0] = numbers[-1]

    elif int(index_) >= len(numbers):
        removed = numbers[-1]
        numbers[-1] = numbers[0]
    else:
        removed = numbers.pop(int(index_))
    removed_sum += removed


    for i in range(len(numbers)):
        if numbers[i]  <= removed:
            numbers[i] += removed
        else:
            numbers[i] -= removed


print(removed_sum)





