given_words = input().split()

comprehension_words = [word for word in given_words if len(word) % 2 ==0]

every_word_on_new_line = [print(''.join(the)) for the in comprehension_words]