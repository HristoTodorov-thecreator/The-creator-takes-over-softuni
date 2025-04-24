key = int(input())

number_lines = int(input())


newword = ''
for i in range(number_lines):
    letter = input()
    x = ord(letter)
    total = x + key
    newletter = chr(total)
    newword += newletter
print(newword)