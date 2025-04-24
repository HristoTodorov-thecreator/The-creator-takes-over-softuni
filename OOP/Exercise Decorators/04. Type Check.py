
def type_check(expected_type):
    def decorator(function):

        def wrapper(*args):
            for i in args:
                if not isinstance(i,expected_type):
                    return f"Bad Type"

            return function(*args)




        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))





