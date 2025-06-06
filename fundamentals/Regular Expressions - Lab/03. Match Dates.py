import  re

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

text = input()

x = re.finditer(pattern,text)

for match in x:

    day = match.group(1)
    month = match.group(3)
    year = match.group(4)

    print(f'Day: {day}, Month: {month}, Year: {year}')