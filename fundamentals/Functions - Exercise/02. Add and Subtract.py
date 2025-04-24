first = int(input())
second = int(input())
third = int(input())




def sum_numbers(first, second):
    return first + second

def subtract(result,third):
     return result - third


def add_and_subtract(first,second,third):
    result = sum_numbers(first,second)
    final_result = subtract(result,third)
    return final_result



print(add_and_subtract(first,second,third))







