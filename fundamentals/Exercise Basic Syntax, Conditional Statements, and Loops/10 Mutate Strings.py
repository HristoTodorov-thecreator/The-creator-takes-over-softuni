first_string = input()
second_string = input()

laststring = first_string

for i in range(len(first_string)):
    leftpart =second_string[:i + 1]
    rightpart =first_string[i+1:]
    newstring = leftpart + rightpart

    if laststring != newstring:
        print(newstring)
        laststring = newstring
