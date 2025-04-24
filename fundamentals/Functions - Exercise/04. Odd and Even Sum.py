number = input()

def oven_and_odd():

    odd_sum = 0
    even_sum = 0


    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 !=0:
            odd_sum += int(i)

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

the_def = oven_and_odd()
print(the_def)