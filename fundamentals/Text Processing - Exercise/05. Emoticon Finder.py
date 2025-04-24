text = input()

for i in range(len(text)):
    if text[i] == ':':
        g = text[i + 1]
        print(f':{g}')