secret_word = input().split()  # Входът ще бъде разделен на думи

list_with_the_words = []


for word in secret_word:

    ascii_numbers = ''
    for char in word:
        if char.isdigit():
            ascii_numbers += char


    first_letter = chr(int(ascii_numbers))
    new_word = ''
    for second in word:
        if not second.isdigit():
            new_word += second
    whole_word_with_number_chr = first_letter + new_word

    new_list = list(whole_word_with_number_chr)





    new_list[1],new_list[-1] = new_list[-1],new_list[1]
    newt = ''
    for n in new_list:
        newt += n
    list_with_the_words.append(newt)

print(' '.join(list_with_the_words))










