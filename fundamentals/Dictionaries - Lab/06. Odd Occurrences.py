words = input().split()

dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

for the_key ,the_value in dict.items():
    if the_value % 2 !=0:
        print(the_key,end= ' ')