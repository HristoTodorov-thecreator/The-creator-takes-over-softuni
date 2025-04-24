commands = int(input())

data_base = {}

for i in range(commands):
    register_ = input().split(' ')
    action = register_[0]
    name = register_[1]
    plate = register_[2] if action == 'register' else None
    if action == 'register':
        if name in data_base:
            print(f'ERROR: already registered with plate number {plate}')


        else:
            data_base[name] = plate
            print(f'{name} registered {plate} successfully')



    elif action == 'unregister':
        if name not in data_base:
            print(f'ERROR: user {name} not found')

        else:
            data_base.pop(name)
            print(f"{name} unregistered successfully")

for i,n in data_base.items():
    print(f'{i} => {n}')

