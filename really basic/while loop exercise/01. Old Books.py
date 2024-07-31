booksearched = 0
what_is_the_book = input()
while True:
    books = input()

    if what_is_the_book == books:
        print(f'You checked {booksearched} books and found it.')
        break
    if books == 'No More Books':
        print(f'The book you search is not here!\nYou checked {booksearched} books.')
        break

    booksearched = booksearched + 1






