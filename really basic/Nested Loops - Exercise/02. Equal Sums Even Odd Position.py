first_number = int(input())
second_number = int(input())


for i in range (first_number , second_number + 1):

    even = 0
    odd = 0
    for idx , digit in enumerate (str(i)):
        if idx % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(i , end= ' ')


