
def fibonacci():
    curr,nextn = 0,1
    while True:
        yield curr
        curr,nextn = nextn , curr + nextn


generator = fibonacci()

for i in range(5):

    print(next(generator))