# Welcome in this program you can search words in text
# Example with text : I am going to the mall
# Example the words you search : am to
# the output is Yes, the word "am" is in the text.
# Yes, the word "to" is in the text.
# you can search it with : AM TO ,am to , Am To
text = input('Please insert your text: ').strip()


search_words = input('Please insert the words you are searching for (separated by spaces): ').strip().split()


for word in search_words:
    if word.lower() in text.lower():
        print(f'Yes, the word "{word}" is in the text.')
    else:
        print(f'No, the word "{word}" is not in the text.')