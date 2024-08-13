students = int(input())

students_failed = 0
student_with_3 = 0
student_with_4 = 0
student_with_perfect = 0

totalrat = 0



for i in range(students):
    rating = float(input())
    if 2 <= rating <= 2.99:
        students_failed += 1
        totalrat += rating


    elif 3 <= rating <= 3.99:
        student_with_3 += 1
        totalrat += rating

    elif 4 <= rating <= 4.99:
        student_with_4 += 1
        totalrat += rating

    elif rating >= 5:
        student_with_perfect += 1
        totalrat += rating



total = student_with_perfect + student_with_4 + student_with_3 + students_failed
print(f"Top students: {student_with_perfect / total * 100:.2f}%")
print(f"Between 4.00 and 4.99: {student_with_4 / total * 100:.2f}%")
print(f"Between 3.00 and 3.99: {student_with_3 / total * 100:.2f}%")
print(f"Fail: {students_failed / total * 100:.2f}%")
print(f"Average: {totalrat / total:.2f}")


