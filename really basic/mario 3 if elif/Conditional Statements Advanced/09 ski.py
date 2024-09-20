days = int(input())  # number of days
type_of_room = input()  # one room , apartment , president apartment
review = input()  # positive or negative

total = 0

overnight_stays = days - 1

if type_of_room == 'room for one person':
    total = 18 * overnight_stays
elif type_of_room == 'apartment':
    total = 25.00 * overnight_stays
elif type_of_room == 'president apartment':
    total = 35.00  * overnight_stays

if days < 10 and type_of_room == 'apartment':
    total= total - (total * 0.30)
elif days <= 15 and type_of_room == 'apartment':
    total = total - (total * 0.35)
elif days > 15 and type_of_room == 'apartment':
    total = total - (total * 0.50)

if days < 10 and type_of_room == 'president apartment':
    total= total - (total * 0.10)
elif days <= 15 and type_of_room == 'president apartment':
    total = total - (total * 0.15)
elif days > 15 and type_of_room == 'president apartment':
    total = total - (total * 0.20)

if review == 'positive':
    total = total + (total * 0.25)
elif review == 'negative':
    total = total - (total * 0.10)

print(f'{total:.2f}')