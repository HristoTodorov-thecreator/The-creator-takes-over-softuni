import re

text_string = input()

pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

x = re.finditer(pattern,text_string)


counter = 0
founded_pairs = {}
for i in x:
    counter += 1
    first_word = i.group(2)
    second_word = i.group(3)
    founded_pairs[first_word] = second_word


if founded_pairs:
    print(f"{counter} word pairs found!")
else:
    print(f'No word pairs found!')

founded_match = []
for m in founded_pairs:
    if m == founded_pairs[m][::-1]:
         founded_match.append(f'{m} <=> {founded_pairs[m]}')
if founded_match:
    print("The mirror words are:")
    print(', '.join(founded_match))



else:
    print(f'No mirror words!')








