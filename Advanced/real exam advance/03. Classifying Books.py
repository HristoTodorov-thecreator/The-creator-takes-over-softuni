
def classify_books(*args,**kwargs):
    fiction_books = []
    non_fiction_books_ = []

    finbooks = []
    non_fin_books = []

    for check,book in args:
        if check == 'fiction':
            fiction_books.append(book)

        elif check == 'non_fiction':
            non_fiction_books_.append(book)

    for t, title in kwargs.items():
        if title in fiction_books:
            finbooks.append(f"{t}#{title}")
        elif title in non_fiction_books_:
            non_fin_books.append(f"{t}#{title}")

    non_fin_books.sort(reverse=True)
    finbooks.sort()

    result = ''

    if finbooks:
        result += "Fiction Books:\n"
        for info in finbooks:
            result += f"~~~{info}\n"

    if non_fin_books:
        result += "Non-Fiction Books:\n"
        for info in non_fin_books:
            result += f"***{info}\n"

    return result

