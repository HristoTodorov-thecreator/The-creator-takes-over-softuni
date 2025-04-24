def vowel_filter(function):

    def wrapper():
        result = []
        vowels = 'aeiou'
        for t in function():
            if t in vowels:
                result.append(t)

        return result


        
        
        
    return wrapper



@vowel_filter

def get_letters():

    return ["a", "b", "c", "d", "e"]


print(get_letters())