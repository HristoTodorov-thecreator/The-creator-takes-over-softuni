season = input()
type_group = input()
number_students = int(input())
night_stand = int(input())

sport = ''
price = 0

if season == 'Winter':
    if type_group == 'mixed':
        price = 10
    elif type_group == 'girls' or type_group == 'boys':
        price = 9.60

elif season == 'Summer':
    if type_group == 'mixed':
        price = 20
    elif type_group == 'girls' or type_group == 'boys':
        price = 15

elif season == 'Spring':
    if type_group == 'mixed':
        price = 9.50
    elif type_group == 'girls' or type_group == 'boys':
        price = 7.20


if season == 'Winter':
    if type_group == 'girls':
        sport = 'Gymnastics'
    elif type_group == 'boys':
        sport = 'Judo'
    elif type_group == 'mixed':
        sport = 'Ski'

if season == 'Spring':
    if type_group == 'girls':
        sport = 'Athletics'
    elif type_group == 'boys':
        sport = 'Tennis'
    elif type_group == 'mixed':
        sport = 'Cycling'

if season == 'Summer':
    if type_group == 'girls':
        sport = 'Volleyball'
    elif type_group == 'boys':
        sport = 'Football'
    elif type_group == 'mixed':
        sport = 'Swimming'

total = price * night_stand * number_students

if number_students >= 50:
    total -= (total * 0.50)
elif 20 <= number_students < 50:
    total -= (total * 0.15)
elif 10 <= number_students < 20:
    total -= (total * 0.05)

print(f"{sport} {total:.2f} lv.")




