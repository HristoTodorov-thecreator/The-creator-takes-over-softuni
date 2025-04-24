text = input()
lastchr = ''

word = ''
for i in text:
    if i == lastchr:
        continue

    word += i


    lastchr = i

print(word)


