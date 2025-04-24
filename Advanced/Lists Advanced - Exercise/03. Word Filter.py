given_words = input().split()

comprehension_words = [word for word in given_words if len(word) % 2 ==0]


for i in comprehension_words:
    print(i)