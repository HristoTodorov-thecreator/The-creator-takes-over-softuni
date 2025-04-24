
def add_grade(student_grades,student_name,grade):
    if student_name not in student_grades:
        student_grades[student_name] = []
    student_grades[student_name].append(grade)



def avarage(grades):
    return sum(grades) / len(grades)


def g(student_grades):
    for name,grade in student_grades.items():
        avaragegr = avarage(grade)
        if avaragegr >= 4.50:
            print(f"{name} -> {avaragegr:.2f}")




def main():
    student_grades = {}
    number_of_students = int(input())

    for i in range(number_of_students):
        student_name = input()
        grade = float(input())
        add_grade(student_grades,student_name,grade)
    g(student_grades)
main()