
class countdown_iterator:
    def __init__(self,count):
        self.count = count + 1
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > self.i:
            self.count -= 1
            i = self.count
            return i
        raise StopIteration



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")





