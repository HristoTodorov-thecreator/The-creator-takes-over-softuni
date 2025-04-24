number = int(input())

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break


print(is_prime)