data = input()

database = {}

while data != 'Season end':

    if '->' in data:
        name, role, points = data.split(' -> ')
        points = int(points)
        database[name] = database.get(name, {})
        if role not in database[name]:
            database[name][role] = points
        else:
            if database[name][role] < points:
                database[name][role] = points
    else:
        nameone,nametwo = data.split(' vs ')

        if nameone in database and nametwo in database:
            for n in database[nameone]:
                if n in database[nametwo]:
                    total_skill_one = sum(database[nameone].values())
                    total_skill_two = sum(database[nametwo].values())
                    if total_skill_one > total_skill_two:
                        del database[nametwo]
                    elif total_skill_two > total_skill_one:
                        del database[nameone]
                    break
    data = input()
sorted_players = sorted(database.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, roles in sorted_players:
    print(f"{player}: {sum(roles.values())} skill")
    sorted_roles = sorted(roles.items(), key=lambda x: (-x[1], x[0]))
    for role, skill in sorted_roles:
        print(f"- {role} <::> {skill}")













