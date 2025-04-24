

class dictionary_iter:
    def __init__(self,g):
        self.g = tuple(g.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.g):
            i = self.i
            self.i += 1

            return self.g[i]
        raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)