user_points = {}
courses = {}

while True:
    result = input().split('-')
    if len(result) == 1:
        break
    if len(result) == 2:
        ban_name = result[0]
        del user_points[ban_name]
    else:
        name,course ,points = result[0],result[1],int(result[2])
        if name not in user_points:
            user_points[name] = 0
        if points > user_points[name]:
            user_points[name] = points
        if course not in courses:
            courses[course] = 0
        courses[course] += 1


print(f'Results:')
for i,n in user_points.items():
    print(f'{i} | {n}')

print(f'Submissions:')
for s,k in courses.items():
    print(f'{s} - {k}')

