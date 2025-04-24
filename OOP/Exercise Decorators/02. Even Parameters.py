
def even_parameters(n):
    def wrapper(*args):
        for i in args:
            if isinstance(i,int):
                if i % 2 == 0:
                    continue
            return  "Please use only even numbers!"
        return n(*args)



    return wrapper

@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))
