number_of_reads = int(input())

speacial_word = input()


list_with_the_text = []
list_with_the_special_word = []



for i in range(number_of_reads):
    text = input()
    list_with_the_text.append(text)
    if speacial_word in text:
        list_with_the_special_word.append(text)


print(list_with_the_text)
print(list_with_the_special_word)



