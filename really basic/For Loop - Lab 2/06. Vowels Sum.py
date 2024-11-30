def sum_vowel_values(word):

    vowel_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

    total = 0

    for letter in word:

        if letter in vowel_values:
            total += vowel_values[letter]

    return total

word = input()

print(sum_vowel_values(word))