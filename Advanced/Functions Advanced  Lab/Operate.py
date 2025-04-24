
def operate(operator,*args):
    result = args[0]

    operations = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y

    }

    if operator in '+-*/':

        for i in args[1:]:
            result = operations[operator](result,i)
        return result



print(operate("*", 3, 4))
