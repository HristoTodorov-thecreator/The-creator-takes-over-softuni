phonebook = {}

while True:
    phone = input()
    if '-' not in phone:
        break
    name,number = phone.split('-')
    phonebook[name] = number

g = int(phone)
for i in range(g):
    search = input()
    if search in phonebook:
        print(f'{search} -> {phonebook[search]}')
    else:
        print(f'Contact {search} does not exist.')


