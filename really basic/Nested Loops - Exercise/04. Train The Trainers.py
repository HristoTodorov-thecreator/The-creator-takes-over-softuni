Jury = int(input())

totalgrade = 0
totalgradessum = 0

while True:
        name_of_presentation = input()
        if name_of_presentation == 'Finish':
            break

        grades = 0



        for i in range (Jury):



             grades += float(input())
        totalgrade += Jury

        totalgradessum += grades

        print(f' {name_of_presentation} - {grades / Jury:.2f}.')

print(f"Student's final assessment is {totalgradessum / totalgrade:.2f}. ")