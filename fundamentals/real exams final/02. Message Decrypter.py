import re

number = int(input())

pattern = r'(%|\$)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$'

for i in range(number):
    message = input()

    x = re.match(pattern,message)
    list = []
    if x:
        word = x.group(2)
        firstnum = int(x.group(3))
        sectnum = int(x.group(4))
        thirdnum = int(x.group(5))
        list.append(firstnum)
        list.append(sectnum)
        list.append(thirdnum)
        theword = ''
        for s in list:
            theword += chr(s)

        print(f'{word}: {theword}')









    else:
        print(f'Valid message not found!')



