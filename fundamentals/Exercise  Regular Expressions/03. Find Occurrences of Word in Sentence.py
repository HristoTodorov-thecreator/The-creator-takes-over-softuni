import re

text = input()
second_text = input()

pattern = fr'(?i)\b{second_text}\b'


x = re.findall(pattern,text)

print(len(x))