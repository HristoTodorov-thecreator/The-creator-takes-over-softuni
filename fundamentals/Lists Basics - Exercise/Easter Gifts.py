gifts = input().split()



while True:
    command = input()

    command_in_pieces = command.split()

    if command == 'No Money':
        break

    if command_in_pieces[0] == 'OutOfStock':
        current_gift = command_in_pieces[1]
        for onegift in range(len(gifts)):
            if current_gift == gifts[onegift]:
                gifts[onegift] = 'None'

    elif command_in_pieces[0] == 'Required':
        current_gift = command_in_pieces[1]
        index = int(command_in_pieces[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif command_in_pieces[0] == 'JustInCase':
        current_gift = command_in_pieces[1]
        gifts[-1] = current_gift

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))

