words = input().split()
searched_word = input()


result = [word for word in words if word == word[::-1]]
counter = 0
for i in result:
    if searched_word == i:
        counter += 1

print(result)
print(f'Found palindrome {counter} times')
