import re

pattern = r'(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))'

text = input()

x = re.finditer(pattern,text)

for m in x:
    print(m.group(0),end=' ')