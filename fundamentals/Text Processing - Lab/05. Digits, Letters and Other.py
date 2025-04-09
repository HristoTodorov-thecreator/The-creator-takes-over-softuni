text = input()


letters_list = [
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f",
    "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l",
    "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r",
    "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x",
    "Y", "y", "Z", "z"
]


numbers = ''
letters = ''
other = ''


for i in text:

    if i.isdigit():
        numbers += i
    elif i in letters_list:
        letters += i
    else:
        other += i

print(numbers)
print(letters)
print(other)