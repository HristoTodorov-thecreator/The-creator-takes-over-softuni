string = list(input())

the = []
for i in range(len(string)):
    if string[i] == '(':
        the.append(i)
    elif string[i] == ')':
        end = i + 1
        start = the.pop()
        print(''.join(string[start:end]))


