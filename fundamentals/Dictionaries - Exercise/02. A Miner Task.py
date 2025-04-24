

new = {}
while True:
    command = input()
    if command == 'stop':
       break
    special_items_number = int(input())
    if command not in new:
        new[command] = 0
    new[command] += special_items_number

for key,value in new.items():
    print(f'{key} -> {value}')