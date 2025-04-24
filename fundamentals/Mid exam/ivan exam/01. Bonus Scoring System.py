number_students = int(input())
number_of_lectures = int(input())
additional_hours = int(input())

max_bonus = 0
max_lectures = 0


total_bonus = 0
for i in range(number_students):
    attendance_student = int(input())
    if attendance_student > max_lectures:
        max_lectures = attendance_student
    if number_of_lectures >0:
        total_bonus = (max_lectures) / number_of_lectures * (5 + additional_hours)
    if total_bonus > max_bonus:
        max_bonus = total_bonus



print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_lectures} lectures.')