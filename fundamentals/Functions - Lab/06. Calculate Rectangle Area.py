width = int(input())
height = int(input())


def calculate():
    result = lambda a ,b : a * b
    t = result(width , height)
    return t

this_is_the_result = calculate()

print(this_is_the_result)
