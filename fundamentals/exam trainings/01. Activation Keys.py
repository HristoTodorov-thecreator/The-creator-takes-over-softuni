key = input()

while True:
    command = input()
    if command == 'Generate':
        break
    splitted = command.split('>>>')

    action = splitted[0]
    if action == 'Contains':
        substring = splitted[1]
        if substring in key:
            print(f'{key} contains {substring}')

        else:
            print(f"Substring not found!")



    if action == 'Flip':
        upper_or_lower = splitted[1]
        startindexone = int(splitted[2])
        endindextwo = int(splitted[3])

        theword = key[startindexone:endindextwo]
        newword = ''
        if upper_or_lower == 'Lower':
            newword = theword.lower()

        elif upper_or_lower == 'Upper':
            newword = theword.upper()

        key = key[:startindexone] +newword + key[endindextwo:]
        print(key)
    if action == 'Slice':
        startindex = int(splitted[1])
        endindex = int(splitted[2])

        key = key[:startindex] + key[endindex:]
        print(key)


print(f"Your activation key is: {key}")