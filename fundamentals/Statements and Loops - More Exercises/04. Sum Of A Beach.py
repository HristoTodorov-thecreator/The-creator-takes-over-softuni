
import re
words = input()


list_ = []

list_.append(words.lower())

pattern = r'sun|fish|water|sand'


for i in list_:


    x = re.finditer(pattern,i)

    counter = 0
    for n in x:

        counter += 1
    print(counter)








