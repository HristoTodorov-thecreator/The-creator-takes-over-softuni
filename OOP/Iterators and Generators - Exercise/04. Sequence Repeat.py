

class sequence_repeat:
    def __init__(self,seq,number):
        self.seq = list(seq)
        self.number = number
        self.i = -1
        self.m = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.m:
            self.m += 1
            self.i += 1
            g = self.i

            if self.i == len(self.seq) - 1:
                self.i = -1


            return self.seq[g]
        raise StopIteration



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')