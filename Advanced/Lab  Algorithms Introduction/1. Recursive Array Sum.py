
def recursive_sum(arr,indx=0):
    if indx == len(arr):
        return 0
    return arr[indx] + recursive_sum(arr, indx + 1)

numbers = [int(x) for x in input().split()]


result = recursive_sum(numbers)
print(result)
