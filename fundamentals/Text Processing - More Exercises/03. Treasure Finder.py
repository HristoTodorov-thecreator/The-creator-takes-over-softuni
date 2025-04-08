numbers = [int(t) for t in input().split()]





while True:
    command = input()
    if command == 'find':
        break



    message = ''
    counter = 0
    for s in range(len(command)):

        if counter < len(numbers):
            word = chr(ord(command[s]) - numbers[counter])
        else:
            counter = 0
            word = chr(ord(command[s]) - numbers[counter])

        message += word

        counter += 1

    g = ''
    second_counter = 0
    the_word = ''
    flag_ = False
    second_wordt = ''
    for o in message:
        if o == '>':
            break
        if flag_:
            second_wordt += o


        if second_counter == 1 and o != '&':
            g += o
        if o == '&':
            second_counter += 1

        if o == '<':
            flag_ = True

    print(f'Found {g} at {second_wordt}')







