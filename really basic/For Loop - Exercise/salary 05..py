
number_of_opensites = int(input())
Salary = int(input())


for _ in range(number_of_opensites):
    name_of_web = input()
    if name_of_web == 'Facebook':
        Salary = Salary - 150
    elif name_of_web == 'Instagram':
        Salary = Salary - 100
    elif name_of_web == 'Reddit':
        Salary = Salary - 50

    if Salary <= 0:
       print(f'You have lost your salary.')
       break

else:
    print(f'{Salary}')