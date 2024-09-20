age = float(input())
name = input()

if name == 'm':
    if age < 16:
        print('Master')
    elif age >= 16:
        print('Mr.')

elif name == 'f':
    if age < 16:
        print('Miss')
    elif age >= 16:
        print('Ms.')
