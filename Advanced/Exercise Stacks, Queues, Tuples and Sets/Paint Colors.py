line = input().split()


main_colors = {'red','blue','yellow'}

secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']

}
founded_colors = []
last = ''
while line:
    first = line.pop(0)
    last = line.pop(-1) if line else ""

    result1 = first + last
    result2 = last + first

    if result1 in main_colors or result1 in secondary_colors:
        founded_colors.append(result1)
    elif result2 in main_colors or result2 in secondary_colors:
        founded_colors.append(result2)
    else:
        if len(first) > 1:
            line.insert(len(line) //2,first[:-1])
        if len(last) > 1:
            line.insert(len(line) //2,last[:-1])


for color in founded_colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in founded_colors:
                founded_colors.remove(color)
                break


print(founded_colors)







