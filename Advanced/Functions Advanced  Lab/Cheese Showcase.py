
def sorting_cheeses(**kwargs):
    sorted_one = sorted(kwargs.items(),key=lambda kvp: (-len(kvp[1]),kvp[0]))
    result = ''
    for i,n in sorted_one:
        result += i + '\n'

        for s in sorted(n,reverse=True) :
            result += f'{s}\n'

    return result[:-1]











print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)