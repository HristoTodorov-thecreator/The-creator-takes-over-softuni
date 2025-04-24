first = int(input())
second = int(input())

def check(number):
    for i in range(1,number):
        number = number * i
    return number


def devided():
    return first_factorial / second_factorial




first_factorial = check(first)
second_factorial = check(second)

t = devided()

print(f'{t:.2f}')