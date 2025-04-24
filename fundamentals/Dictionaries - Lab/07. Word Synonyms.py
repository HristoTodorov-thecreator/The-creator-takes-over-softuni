n = int(input())

synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for t in synonyms:
    print(f'{t} - {", ".join(synonyms[t])}')