
class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity
        self.__length = 0


    def add(self,key,value):
        self[key] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f'not found in hash table')

    def get(self,key,message=None):
        try:
            return self[key]

        except KeyError:
            return message


    def __setitem__(self, key, value):
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
        except ValueError:
            pass
        else:
            return

        if len(self) == self.__max_capacity:
            self.__resize()
        index = self.__calc_index(key)

        self.__keys[index] = key
        self.__values[index] = value

        self.__length += 1


    def __calc_index(self,key):

        index=  sum(ord(c)for c in key) % self.__max_capacity

        index = self.__get_index(index)

        return index

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity

        self.__max_capacity *= 2


    def __len__(self):
        return self.__length


    def __get_index(self,index):
        while True:
            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity

            index += 1

    def __str__(self):
        result = []

        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                result.append(f'{self.__keys[i]}: {self.__values[i]}')

        return '{' + ', '.join(result) + '}'

    def remove_item(self,key):
        try:
            i = self.__keys.index(key)
            self.__keys[i] = None
            self.__values[i] = None
            self.__length -= 1
        except ValueError:
            raise KeyError(f"Key '{key}' not found in hash table")

