

def working_a_day():
    working_employees = 3



def inputs_for_efficiency():
    firstone = int(input())
    secondone = int(input())
    thirdone = int(input())
    return firstone ,secondone,thirdone
def student_count():
    students = int(input())
    return students


def calculate():
    firstone , secondone , thirdone = inputs_for_efficiency()
    students = student_count()

    hr = firstone + secondone + thirdone


    counter = 0


    while students > 0:
        counter += 1
        if counter % 4 == 0:
            continue
        students -= hr

    print(f'Time needed: {counter}h.')

calculate()



