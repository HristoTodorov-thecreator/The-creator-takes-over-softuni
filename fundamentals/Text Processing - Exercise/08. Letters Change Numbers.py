strings = input().split()


total = 0

position_lettters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                     'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


for i in strings:
    first_letter = i[0]

    number = ''.join([char for char in i if char.isdigit()])
    number = int(number)


    if first_letter.isupper():


        total += (int(number) / position_lettters[first_letter])

    elif i[0].islower():
        bigletter = first_letter.upper()

        total += (int(number) * position_lettters[bigletter])

    if i[-1].isupper():
        lastletter = i[-1]

        total -= position_lettters[lastletter]


    elif i[-1].islower():
        lastletter = i[-1].upper()


        total += position_lettters[lastletter]

print(f'{total:.2f}')




