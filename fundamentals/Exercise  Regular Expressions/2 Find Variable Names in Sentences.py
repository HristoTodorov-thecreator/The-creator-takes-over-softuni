import re

text = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

x = re.findall(pattern,text)



print(','.join(x))
