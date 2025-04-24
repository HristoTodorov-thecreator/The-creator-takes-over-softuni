number_of_students = int(input())

t = {}

for i in range(number_of_students):
    student ,grade = tuple(input().split())
    grade = float(grade)

    if student not in t:
        t[student] = []
    t[student].append(grade)

for m in t:
    the_sum = sum(t[m])
    len_ = len(t[m])
    avarage = the_sum / len_
    print(f'{m} -> {" ".join(f"{grade:.2f}" for grade in t[m])} (avg: {avarage:.2f})')






