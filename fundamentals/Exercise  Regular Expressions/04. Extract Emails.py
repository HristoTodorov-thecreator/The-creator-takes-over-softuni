import re

text = input()

pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'


x = re.findall(pattern,text)

for i in x:
    print(i[0])