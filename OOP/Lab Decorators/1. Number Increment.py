def number_increment(numbers):

    def increase():
        result = []
        for i in numbers:
            result.append(i + 1)

        return result


    return increase()



print(number_increment([1, 2, 3]))