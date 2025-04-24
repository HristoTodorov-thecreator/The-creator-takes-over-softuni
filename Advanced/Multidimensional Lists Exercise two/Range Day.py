SIZE = 5

def move(direction,steps):
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == 'x':
        return my_position
    return [r,c]

def shoot(direction,):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0<= r <SIZE and 0<= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r,c]

        r+= directions[direction][0]
        c += directions[direction][1]



field = []

targets = 0

targets_hit = 0


targets_hit_positions = []
my_position = []


directions = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right':(0,1),


}

for row in range(SIZE):
    the_row = input().split()

    field.append(the_row)
    targets += field[row].count('x')
    for s in range(len(the_row)):
        if field[row][s] == 'A':
            my_position = [row,s]



for i in range(int(input())):

    command_info = input().split()

    if command_info[0] == 'move':
        my_position = move(command_info[1],int(command_info[2]))
    elif command_info[0] == 'shoot':
        target_down = shoot(command_info[1])

        if target_down:
            targets_hit_positions.append(target_down)
            targets_hit +=1

        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break

if targets_hit < targets:
    print(f'Training not completed! {targets - targets_hit} targets left.')

print(*targets_hit_positions,sep='\n')



