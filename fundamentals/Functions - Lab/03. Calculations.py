operation = input()

first_number = int(input())
second_number = int(input())




def calculator():
    def addition():
        return first_number + second_number

    def subtraction():
        return first_number - second_number

    def multiplication():
        return first_number * second_number

    def divide():
        return int(first_number / second_number)



    if operation == 'add':
        return addition()
    elif operation == 'subtract':
        return subtraction()
    elif operation == 'multiply':
        return multiplication()
    elif operation == 'divide':
        return divide()


result = calculator()

print(result)
