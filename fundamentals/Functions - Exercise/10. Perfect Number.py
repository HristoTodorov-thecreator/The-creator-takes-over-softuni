given_number = int(input())

def check():
    sum_devisor = 0

    for i in range(1,given_number):
        if given_number % i == 0:
            sum_devisor += i

    if sum_devisor == given_number:
        return f'We have a perfect number!'
    return f"It's not so perfect."

print(check())
