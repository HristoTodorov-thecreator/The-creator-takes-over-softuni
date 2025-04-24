

def students_credits(*args):
    courses_score = {}
    g = []
    total = 0
    for info in args:
        course_name, course_credits, max_test_points, dian_points = info.split("-")
        current_percentage = int(dian_points) / int(max_test_points)
        diyan_current_credits = current_percentage * int(course_credits)
        total += diyan_current_credits
        courses_score[course_name] = diyan_current_credits

    if total >= 240:
        g.append(f"Diyan gets a diploma with {total:.1f} credits.")
    else:
        g.append(f"Diyan needs {240 - total:.1f} credits more for a diploma.")

    for k, v in sorted(courses_score.items(), key=lambda x: -x[1]):
        g.append(f"{str(k)} - {float(v):.1f}")

    return '\n'.join(g)





print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)