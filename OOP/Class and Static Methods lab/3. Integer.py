from math import floor

class Integer:
    def __init__(self,value):
        self.value = value

    @classmethod
    def from_float(cls,float_value):
        if not isinstance(float_value,float):
            return f'value is not a float'

        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in reversed(value):
            num = roman_numerals[char]
            if num < prev_value:
                total -= num
            else:
                total += num
            prev_value = num

        return cls(total)

    @classmethod
    def from_string(cls,value):
        if not isinstance(value,str):
            return 'wrong type'
        try:
            return cls(int(value))
        except ValueError:
            return f'wrong type'

first_num = Integer(10)

print(first_num.value)


second_num = Integer.from_roman("IV")

print(second_num.value)


print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))