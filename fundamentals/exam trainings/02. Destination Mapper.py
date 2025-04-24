import re

text = input()

pattern = r"(=|\/)[A-Z][a-zA-Z]{2,}\1"

x = re.finditer(pattern,text)



list = []
points = 0
for match in x:
    word = match.group()

    if '=' in word:
        newword = word.replace('=','')
        list.append(newword)
        po = len(newword)
        points += po


    else:
        newword = word.replace('/','')
        list.append(newword)
        po = len(newword)
        points += po




print(f'Destinations: {", ".join(list)}')
print(f'Travel Points: {points}')
