import re

text = input()



pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

x = re.findall(pattern,text)


for i in range(len(x)):
    if i < len(x) - 1:
        print(x[i],end=', ')
    else:
        print(x[i])