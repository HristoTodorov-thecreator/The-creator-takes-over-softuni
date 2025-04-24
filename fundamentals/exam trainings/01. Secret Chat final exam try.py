def secret_message():
    secret = input()
    while True:
        command = input()
        if command == 'Reveal':
            break
        splitted = command.split(':|:')
        firstcommand = splitted[0]
        if firstcommand == 'ChangeAll':
            sub = splitted[1]
            replace = splitted[2]
            secret = secret.replace(sub,replace)
            print(secret)
        if firstcommand == 'Reverse':
            subs = splitted[1]
            if subs in secret:
                g = subs[::-1]
                secret = secret.replace(subs,'')
                secret = secret + g
                print(secret)


            else:
                print(f"error")
        if firstcommand == 'InsertSpace':

            index_ = int(splitted[1])
            secret = secret[:index_] + ' ' + secret[index_:]
            print(secret)


    return secret
print(f'You have a new text message: {secret_message()}')


