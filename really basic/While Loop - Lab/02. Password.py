username = input()
password = input()

data = ''
while data != password:
    data = input()
else:
    print(f'Welcome {username}!')

