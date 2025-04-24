words = input().split(', ')


list = []



def third_check(i):
    if ' ' in i:
        return False
    return True



def second_check(i):

    if i.isalnum() or '-' in i or '_' in i:


        return True
    return False






def letters(i):
    if 3 <= len(i) <=16:
        return True
    return False

for i in words:
    if letters(i) and third_check(i) and second_check(i):
        list.append(i)

for n in list:
    print(n)

