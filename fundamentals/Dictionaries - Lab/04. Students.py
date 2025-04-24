

people = []

while True:

    info = input()

    if ':' not in info:
        g = info.replace('_',' ')
        break

    first_name,special_number,course = info.split(':')
    people.append({'name':first_name,'id' : special_number,'course':course} )

for s in people:
    if g == s['course']:
        print(f'{s["name"]} - {s["id"]}')


