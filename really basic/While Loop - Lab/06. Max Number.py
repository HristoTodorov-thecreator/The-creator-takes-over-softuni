from sys import maxsize
max_number = -maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    text = int(text)
    if max_number < text:
        max_number = text

print(max_number)








