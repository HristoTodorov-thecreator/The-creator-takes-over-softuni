students = int(input())
groupone = 0
grouptwo = 0
groupthree = 0
groupfour = 0

total = 0


for i in range(students):
    rating = float(input())

    if rating >= 5:
        groupone += 1
        total += rating
    elif rating > 3.99:
        grouptwo += 1
        total += rating
    elif rating > 2.99:
        groupthree += 1
        total += rating
    elif rating > 1.99:
        groupfour += 1
        total += rating


percentgroupone = (groupone / students) * 100
percentgrouptwo = (grouptwo / students) * 100
percentgroupthree = (groupthree / students) * 100
percentgroupfour = (groupfour / students) * 100



print(f'Top students: {percentgroupone:.2f}%')
print(f'Between 4.00 and 4.99: {percentgrouptwo:.2f}%')
print(f'Between 3.00 and 3.99: {percentgroupthree:.2f}%')
print(f'Fail: {percentgroupfour:.2f}%')
print(f'Average: {total / students:.2f}')
