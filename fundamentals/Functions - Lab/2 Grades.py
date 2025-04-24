grade_ = float(input())


def grades():
    if 2 <= grade_ <= 2.99:
        return 'Fail'
    elif 3 <= grade_ <= 3.49:
        return 'Poor'
    elif 3.50 <= grade_ <= 4.49:
        return 'Good'
    elif 4.50 <= grade_ <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_ <= 6:
        return 'Excellent'

result = grades()

print(result)