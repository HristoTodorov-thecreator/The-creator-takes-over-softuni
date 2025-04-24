given_numbers = input().split(', ')

def positive_():
    return [number for number in given_numbers if int(number) >= 0]

def negative_():
    return [number for number in given_numbers if int(number) < 0]

def even_():
    return [number for number in given_numbers if int(number) % 2 ==0]

def odd_():
    return [number for number in given_numbers if int(number) % 2 !=0]

print(f"Positive: {', '.join(positive_())}")
print(f"Negative: {', '.join(negative_())}")
print(f"Even: {', '.join(even_())}")
print(f"Odd: {', '.join(odd_())}")