sum_prime = 0
sum_non_prime = 0


while True:
    command = input()

    if command == 'stop':
        break

    number = int(command)
    if number < 0:
        print(f'Number is negative.')
        continue




    for i in range(2 , number):
        if number % i == 0:

            sum_non_prime += number
            break

    else:
        sum_prime += number

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
