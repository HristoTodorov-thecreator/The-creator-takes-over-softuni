number_of_electrons = int(input())

list_shells = []
n = 0
while number_of_electrons > 0:
    n += 1
    maximum_for_shell = 2 * n ** 2
    if maximum_for_shell > number_of_electrons:
        list_shells.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    else:
        list_shells.append(maximum_for_shell)
        number_of_electrons -= maximum_for_shell

print(list_shells)

