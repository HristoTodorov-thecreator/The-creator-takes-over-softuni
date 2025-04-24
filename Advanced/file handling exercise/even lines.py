symbols = ("-", ",", ".", "!", "?")

with open('files_/file1.txt', 'r') as v_lines_file:
    text = v_lines_file.readlines()

for i in range(0,len(text),2):

    for symbol in symbols:

        text[i] = text[i].replace(symbol,'@')


    print(*text[i].split()[::-1])

