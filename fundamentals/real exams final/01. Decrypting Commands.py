string = input()

while True:
    command = input()
    if command == 'Finish':
        break
    splited = command.split()
    action = splited[0]
    if action == 'Replace':
        currentchar = splited[1]
        newchar = splited[2]
        if currentchar in string:

            string = string.replace(currentchar,newchar)
            print(string)

    if action == 'Cut':
        startind = int(splited[1])
        endind = int(splited[2])
        length = len(string)
        if 0<= startind < length and 0<= endind < length:
            string = string[:startind] + string[endind + 1:]
            print(string)

        else:
            print(f'Invalid indices!')

    if action == 'Make':
        lower_or_upper = splited[1]
        if lower_or_upper == 'Upper':
            string = string.upper()
            print(string)

        elif lower_or_upper == 'Lower':
            string = string.lower()
            print(string)

    if action == 'Check':
        message = splited[1]
        if message in string:
            print(f"Message contains {message}")
        else:
            print(f"Message doesn't contain {message}")

    if action == 'Sum':
        startindex = int(splited[1])
        endindex = int(splited[2])

        if 0 <= startindex < len(string) and 0 <= endindex < len(string):

             second_word = string[startindex:endindex + 1]
             total = 0
             for s in second_word:
                 numbert = ord(s)
                 total += numbert
             print(total)
        else:
            print(f'Invalid indices!')

