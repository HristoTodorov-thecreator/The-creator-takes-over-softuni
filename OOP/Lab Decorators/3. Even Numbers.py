def even_numbers(function):

    def wrapper(numbers):
        result = []
        for i in numbers:
            if i % 2 == 0:
                result.append(i)
        return result



    return wrapper



@even_numbers

def get_numbers(numbers):

    return numbers

print(get_numbers([1, 2, 3, 4, 5]))