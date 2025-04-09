first_word = input()
second_word = input()

while first_word in second_word:
    second_word = second_word.replace(first_word,'')

print(second_word)