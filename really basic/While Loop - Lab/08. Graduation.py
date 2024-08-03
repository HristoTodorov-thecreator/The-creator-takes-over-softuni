name = input()

class_ = 0
failclass = 0
totalrating = 0

while True:
    numberrating = float(input())
    if 4 <= numberrating <= 6:
        class_ = class_ + 1
        totalrating = totalrating + numberrating
    elif numberrating < 4:

        failclass = failclass + 1




    if failclass >= 2:
        print(f'{name} has been excluded at {class_ + 1} grade')
        break
    elif class_ >= 12:
        print(f'{name} graduated. Average grade: {totalrating / class_:.2f}')
        break


