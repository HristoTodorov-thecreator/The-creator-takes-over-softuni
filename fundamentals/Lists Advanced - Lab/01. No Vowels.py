theword = input()

list_with_letters = ['a', 'o', 'u', 'e', 'i']


g = [i for i in theword if i.lower() not in list_with_letters]



print(''.join(g))