import os

while True:
    command,*info = input().split('-')

    if command == 'Create':

        with open(f'files/{info[0]}','w'): pass


    elif command == 'Add':
        with open(f'files/{info[0]}', 'a') as f:
            f.write(f'{info[1]}\n')

    elif command == 'Replace':
        try:
            with open(f'files/{info[0]}','r+') as f:
                text = f.read()
                text = text.replace(info[1],info[2])

                f.seek(0)
                f.write(text)
                f.truncate()

        except FileNotFoundError:
            print(f'Error')

    elif command == 'Delete':
        try:
            os.remove(f'files/{info[0]}')

        except FileNotFoundError:
            print(f'Error')
    elif command == 'End':
        break



