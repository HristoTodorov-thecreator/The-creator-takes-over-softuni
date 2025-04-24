

field_size = int(input())

commands = [x for x in input().split()]

fields = []
coal_count = 0
r,c = 0,0
for i in range(field_size):
    field = input().split()
    for s in range(len(field)):
        if field[s] == 's':
            r,c = i,s

        if field[s] == 'c':
            coal_count += 1


    fields.append(field)

def check (row,col,size):
    return 0 <= row < size and 0 <= col < size

for command in commands:

    next_r, next_c = r, c

    if command == "up":
        next_r -= 1
    elif command == "down":
        next_r += 1
    elif command == "left":
        next_c -= 1
    elif command == "right":
        next_c += 1
    if check(next_r,next_c,field_size):
        r,c = next_r,next_c

        if fields[r][c] == "c":
            fields[r][c] = "*"
            coal_count -= 1
            if coal_count == 0:
                print(f"You collected all coal! ({r}, {c})")
                break

        elif fields[r][c] == "e":
            print(f"Game over! ({r}, {c})")
            break
else:

    print(f"{coal_count} pieces of coal left. ({r}, {c})")








