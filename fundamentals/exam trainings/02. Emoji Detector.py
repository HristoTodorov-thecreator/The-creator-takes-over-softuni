import re

pattern = r'(:{2})[A-Z][a-z]{2,}\1|(\*\*)[A-Z][a-z]{2,}(\*\*)'



string_ = input()
listt = 1
for char in string_:
    if char.isdigit():
        listt *= int(char)
print(f'Cool threshold: {listt}')
x = re.finditer(pattern,string_)
list_with_emojy = []
for m in x:

    list_with_emojy.append(m.group())

print(f'{len(list_with_emojy)} emojis found in the text. The cool ones are:')
cool_ones = []

for n in list_with_emojy:
    second_total = 0
    for u in n:
        if u == ':' or u == '*':
            continue

        second_total += ord(u)

    if second_total > listt:
        cool_ones.append(n)
if cool_ones:

    for q in cool_ones:
        print(q)