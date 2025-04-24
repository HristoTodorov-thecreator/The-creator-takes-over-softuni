
class custom_range:
    def __init__(self,start,end):
        self.start = start
        self.end = end

        self.t = self.start - 1

    def __iter__(self):
        return self


    def __next__(self):
        self.t += 1
        if self.t > self.end:
            raise StopIteration
        return self.t
