sum_ = 0
word_the_most_points = 0
list_ = ['a','e','i','o','u','y','A','E','O','Y','I','U']
word_name_p = ''
while True:
    word = input()
    if word == 'End of words':
        break
    n = len(word)
    for i in word:
        sum_ += ord(i)
    if word[0] in list_:
        sum_ = sum_ * n
    else:
        sum_ = sum_ / n

    if sum_ > word_the_most_points:
        word_the_most_points = sum_
        word_name_p = word
    sum_ = 0
print(f"The most powerful word is {word_name_p} - {word_the_most_points}" )


