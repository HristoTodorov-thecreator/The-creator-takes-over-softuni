message = input()



while True:
    command = input().split('|')
    if command[0] == 'Decode':





        print(f'The decrypted message is: {message}')
        break
    if command[0] == 'Move':
        number_of_letters = int(command[1])

        message = message[number_of_letters:] + message[:number_of_letters]
    if command[0] == 'Insert':
        index_ = int(command[1])
        value_ = command[2]

        message = message[:index_] + value_ + message[index_:]



    if command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)







