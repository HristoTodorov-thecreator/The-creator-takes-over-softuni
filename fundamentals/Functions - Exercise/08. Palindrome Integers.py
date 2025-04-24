inputnumbers = input().split(', ')


def check():
    for num in inputnumbers:
        ispalli = num
        palli2 = num[::-1]
        if ispalli == palli2:
            print(f'True')
        else:
            print(f'False')





check()