numbers = [int(i) for i in input().split()]

command = input().split()

while command[0] != "end":

    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")


    elif command[0] == "max":

        odd_or_even = command[1]

        max_value = -float('inf')

        max_index = -1

        for index, number in enumerate(numbers):

            if (odd_or_even == "even" and number % 2 == 0) or (odd_or_even == "odd" and number % 2 != 0):

                if number >= max_value:
                    max_value = number

                    max_index = index

        if max_index != -1:

            print(max_index)

        else:

            print("No matches")


    elif command[0] == "min":

        odd_or_even = command[1]

        min_value = float('inf')

        min_index = -1

        for index, number in enumerate(numbers):

            if (odd_or_even == "even" and number % 2 == 0) or (odd_or_even == "odd" and number % 2 != 0):

                if number <= min_value:
                    min_value = number

                    min_index = index

        if min_index != -1:

            print(min_index)

        else:

            print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        if 0 < count <= len(numbers):
            if command[2] == "even":
                print(even[:count])
            elif command[2] == "odd":
                print(odd[:count])
        else:
            print("Invalid count")

    elif command[0] == "last":
        count = int(command[1])
        if 0 < count <= len(numbers):
            if command[2] == "even":
                print(even[-count:])
            elif command[2] == "odd":
                print(odd[-count:])
        else:
            print("Invalid count")


    command = input().split()

print(numbers)