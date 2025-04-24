from collections import deque

def age_assignment(*args,**kwargs):

    result = deque()
    for key,value in kwargs.items():
        for name in args:
            if name.startswith(key):
                result.append(f'{name} is {value} years old.')
                break


    return '\n'.join(sorted(result))










print(age_assignment("Peter", "George", G=26, P=19))