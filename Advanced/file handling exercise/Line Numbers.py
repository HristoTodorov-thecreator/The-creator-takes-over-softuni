from string import punctuation

with open('files_/file1.txt', 'r') as txt:

    text = txt.readlines()


text2 = open('files_/texttry.txt', 'w')



counter = 1
for i in text:
    i = i.replace('\n','')
    letters = 0
    other = 0
    for s in i:
        if s.isalpha():
            letters +=1
        if s in punctuation:
            other += 1


    text2.write(f'Line {counter}: {i} ({letters})({other})\n')
    counter += 1

text2.close()