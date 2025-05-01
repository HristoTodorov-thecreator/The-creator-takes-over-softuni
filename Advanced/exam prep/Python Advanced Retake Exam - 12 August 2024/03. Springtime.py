
def start_spring(**kwargs):
    groups = {}
    for name,type in kwargs.items():
        if type not in groups:
            groups[type] = []
        groups[type].append(name)

    for value in groups.values():
        value.sort()

    sorted_groups = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    result = []
    for type,items in sorted_groups:
        result.append(f"{type}:")
        for item in items:
            result.append(f"-{item}")

    return '\n'.join(result)







example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))