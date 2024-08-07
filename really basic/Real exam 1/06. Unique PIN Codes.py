
upper_limit1 = int(input())
upper_limit2 = int(input())
upper_limit3 = int(input())


for digit1 in range(2, upper_limit1 + 1, 2):
    for digit2 in range(2, upper_limit2 + 1):

        if digit2 == 2 or digit2 == 3 or digit2 == 5 or digit2 == 7:
            for digit3 in range(2, upper_limit3 + 1, 2):

                print(f"{digit1} {digit2} {digit3}")
