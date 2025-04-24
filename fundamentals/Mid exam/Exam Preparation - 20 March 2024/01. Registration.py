username = input()


while True:
    command = input().split()
    if command[0] == 'Registration':
        break
    if command[0] == 'Letters':
        if command[1] == 'Lower':
            username = username.lower()
            print(f'{username}')

        if command[1] == 'Upper':
            username = username.upper()
            print(f'{username}')




    if command[0] == 'Reverse':
        firstindex = int(command[1])
        secondindex = int(command[2])
        if 0 <= firstindex < len(username) and 0 <= secondindex <len(username):
            g = username[firstindex:secondindex + 1]
            gt = g[::-1]
            print(f'{gt}')



        else:
            continue


    if command[0] == 'Substring':
        if command[1] in username:
            username = username.replace(command[1],'')
            print(username)

        else:
            print(f"The username {username} doesn't contain {command[1]}.")



    if command[0] == 'Replace':
        if command[1] in username:
            username = username.replace(command[1],'-')
            print(username)

    if command[0] == 'IsValid':
        if command[1] in username:
            print(f'Valid username.')
        else:
            print(f'{command[1]} must be contained in your username.')
