data = input()

database = {}

while data != 'Once upon a time':
    name, color, physics = data.split(" <:> ")
    physics = int(physics)

    if (name,color) not in database:
        database[(name,color)] = physics
    else:
        database[(name, color)] = max(database[(name, color)], physics)




    data = input()

sorting = sorted(database.items(),key=lambda x: (-x[1], -sum(1 for k in database if k[1] == x[0][1])))




for (name, hat_color), physics in sorting:
    print(f"({hat_color}) {name} <-> {physics}")