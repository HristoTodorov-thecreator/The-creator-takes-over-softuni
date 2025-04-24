numbers = input().split()
string = list(input())

message = ''

for n in numbers:
    index = sum(int(digit) for digit in n)

    index %= len(string)
    message += string[index]

    string.pop(index)


print(message)