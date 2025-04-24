first_field = list(map(int,input().split()))
second_field = list(map(int,input().split()))
third_field = list(map(int,input().split()))

if first_field[0] == 2 and first_field[1] == 2 and first_field[2] == 2:
    print(f'Second player won')
    exit()

elif second_field[0] == 2 and second_field[1] == 2 and second_field[2] == 2:
    print(f'Second player won')
    exit()

elif third_field[0] == 2 and third_field[1] == 2 and third_field[2] == 2:
    print(f'Second player won')
    exit()

elif first_field[0] == 2 and second_field[1] == 2 and third_field[2] == 2:
    print(f'Second player won')
    exit()

elif first_field[2] == 2 and second_field[1] == 2 and third_field[0] == 2:
    print(f'Second player won')
    exit()
elif first_field[0] == 2 and second_field[0] == 2 and third_field[0] ==2:
    print(f'Second player won')
    exit()

elif first_field[1] == 2 and second_field[1] == 2 and third_field[1] == 2:
    print(f'Second player won')
    exit()
elif first_field[2] == 2 and second_field[2] == 2 and third_field[2] == 2:
    print(f'Second player won')
    exit()


if first_field[0] == 1 and first_field[1] == 1 and first_field[2] == 1:
    print(f'First player won')
    exit()

elif second_field[0] == 1 and second_field[1] == 1 and second_field[2] == 1:
    print(f'First player won')
    exit()

elif third_field[0] == 1 and third_field[1] == 1 and third_field[2] == 1:
    print(f'First player won')
    exit()

elif first_field[0] == 1 and second_field[1] == 1 and third_field[2] == 1:
    print(f'First player won')
    exit()

elif first_field[2] == 1 and second_field[1] == 1 and third_field[0] == 1:
    print(f'First player won')
    exit()

elif first_field[0] == 1 and second_field[0] == 1 and third_field[0] ==1:
    print(f'First player won')
    exit()

elif first_field[1] == 1 and second_field[1] == 1 and third_field[1] == 1:
    print(f'First player won')
    exit()
elif first_field[2] == 1 and second_field[2] == 1and third_field[2] == 1:
    print(f'First player won')
    exit()

else:
    print(f'Draw!')
    exit()