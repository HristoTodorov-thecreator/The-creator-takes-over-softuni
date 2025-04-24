import re


text = input()
x = []
while text:


    pattern = r'\d+'

    x += re.findall(pattern,text)
    text = input()


for i in x:
    print(i,end=' ')