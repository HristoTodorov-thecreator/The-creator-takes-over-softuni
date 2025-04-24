

def genrange(start,end):
    end += 1

    while start < end:
        yield start
        start += 1


print(list(genrange(1, 10)))