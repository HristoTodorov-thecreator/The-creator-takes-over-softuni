from sys import maxsize
min_number = maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    text = int(text)
    if min_number > text:
        min_number = text

print(min_number)
