


while True:
    strings = input()
    if strings == 'End':
        break
    if strings =='SoftUni':
        continue

    newword = ''

    for i in strings:
        g = 2 * i
        newword += g
    print(newword)



