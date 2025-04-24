def get_magic_triangle(number):
    result = []
    result.append([1])
    result.append([1,1])

    for i in range(2,number):
        prev_row = result[i-1]
        row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, len(prev_row))] + [1]



        result.append(row)

    return result


print(get_magic_triangle(3))