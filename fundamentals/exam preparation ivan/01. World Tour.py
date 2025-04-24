string = input()


while True:
    command = input()
    if command == 'Travel':
        break

    splitted = command.split(':')
    first = splitted[0]
    if first == 'Add Stop':
        index_ = int(splitted[1])
        str = splitted[2]
        if index_ < len(string):
            string = string[:index_] + str + string[index_:]
        print(string)


    if first == 'Remove Stop':
        start = int(splitted[1])
        end = int(splitted[2])
        if start < len(string) and end < len(string):
            element = string[start:end+1]
            string = string.replace(element,'')

        print(string)

    if first == 'Switch':
        oldstr = splitted[1]
        newstr = splitted[2]
        if oldstr in string:
            string = string.replace(oldstr,newstr)

        print(string)

print(f"Ready for world tour! Planned stops: {string}")