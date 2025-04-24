
def words_sorting(*args):
    g = {}
    t = list(args)
    while t:
        for word in args:
            total = 0
            for letter in word:
                total += ord(letter)

            g[word] = total
            t.remove(word)

    total_values = sum(g.values())
    if total_values % 2 == 0:
        output = [f"{key} - {value}" for key, value in sorted(g.items(), key= lambda x: x[0])]
    else:
        output = [f"{key} - {value}" for key, value in sorted(g.items(), key= lambda x: -x[1])]

    return '\n'.join(output)





print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))