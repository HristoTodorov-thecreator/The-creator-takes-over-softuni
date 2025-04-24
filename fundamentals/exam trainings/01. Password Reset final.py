string = input()

while True:
    command = input()
    if command == 'Done':
        break

    splliteed = command.split(' ')
    action = splliteed[0]


    if action == 'TakeOdd':

        secondstring = ''
        for i in range(len(string)):
            if i % 2 != 0:
                secondstring += string[i]
        string = secondstring
        print(string)

    if action == 'Cut':
        ind = int(splliteed[1])
        leng = int(splliteed[2]) + ind
        t = ''
        string = string.replace(string[ind:leng], "", 1)

        print(string)






    if action == 'Substitute':
        first_string = splliteed[1]
        sec_string = splliteed[2]
        if first_string in string:
            string = string.replace(first_string,sec_string)
            print(string)

        else:
            print(f'Nothing to replace!')
print(f'Your password is: {string}')