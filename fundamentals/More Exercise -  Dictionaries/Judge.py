courses, individual = {}, {}
data = input()
while data != "no more time":

    name, course, score = data.split(" -> ")
    courses[course] = courses.get(course, {})
    courses[course][name] = courses[course].get(name, 0)
    courses[course][name] = max(int(score), courses[course][name])
    data = input()

for course in courses:
    print(f"{course}: {len(courses[course])} participants")
    for pos, (user, score) in enumerate(sorted(courses[course].items(), key= lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {user} <::> {score}")
        individual[user] = individual.get(user, 0) + score

print("Individual standings:")
for pos, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {user} -> {score}")