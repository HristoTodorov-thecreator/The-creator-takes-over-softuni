number_not_good_grades = int(input())
bad_grade = 0
taskproblems = 0
gradetotalforavarage = 0
lastproblem = ''
while True:
    task = input()
    if task == 'Enough':
        print(f'Average score: {gradetotalforavarage / taskproblems:.2f}')
        print(f'Number of problems: {taskproblems}')
        print(f'Last problem: {lastproblem}')
        break
    taskproblems += 1
    grade = int(input())
    gradetotalforavarage = gradetotalforavarage + grade
    lastproblem = task

    if grade <= 4:
        bad_grade += 1
    if bad_grade == number_not_good_grades:
        print(f'You need a break, {number_not_good_grades} poor grades.')
        break
