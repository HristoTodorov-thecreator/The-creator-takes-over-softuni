
course_with_password = {}
database = {}
while True:
    g = input()
    if g == 'end of contests':
        break
    splitted = g.split(':')
    course = splitted[0]
    password = splitted[1]
    course_with_password[course] = password

while True:
    t = input()
    if t == 'end of submissions':
        break
    splittedtwo = t.split('=>')
    course = splittedtwo[0]
    password = splittedtwo[1]
    name = splittedtwo[2]
    points = int(splittedtwo[3])
    if course in course_with_password:
        if course_with_password[course] == password:
            if name not in database:
                database[name] = {}
            if course not in database[name] or database[name][course] < points:
                database[name][course] = points


best_user = ''
best_points = 0


for key,cour in database.items():
    total = sum(cour.values())
    if total > best_points:
        best_points = total
        best_user = key

print(f'Best candidate is {best_user} with total {best_points} points.')
print(f'Ranking:')


for name in sorted(database):
    print(name)
    for contest, points in sorted(database[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")





