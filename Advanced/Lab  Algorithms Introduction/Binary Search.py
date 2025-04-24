the_list = [int(x) for x in input().split()]

the_number = int(input())


def bin_search(the_list,the_number):
    left = 0
    right = len(the_list)-1

    while left <= right:
        mid = (left + right) // 2

        mid_el = the_list[mid]
        if mid_el == the_number:
            return mid
        if mid_el < the_number:
            left = mid + 1
        else:
            right = mid - 1


    return -1

print(bin_search(the_list,the_number))