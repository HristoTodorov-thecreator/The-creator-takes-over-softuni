start = int(input())
end = int(input())
magicnumber = int(input())

rotation = 0
flag = False

for x in range (start , end + 1):
    for y in range (start , end + 1):
        rotation += 1
        if x + y == magicnumber:
            print(f'Combination N:{rotation} ({x} + {y} = {magicnumber})')
            flag = True
            break
    if flag:
        break

else:
    print(f'{rotation} combinations - neither equals {magicnumber}')
