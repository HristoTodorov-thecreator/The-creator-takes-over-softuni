string = input()

current_result, result_show, number = "", "", "",

for index, ch in enumerate(string):
    if not ch.isdigit():
        current_result += ch

    elif ch.isdigit():
        number += ch
        if index + 1 < len(string):
            if string[index + 1].isdigit():
                continue
        result_show += int(number) * current_result
        current_result, number = "", ""

result_show = result_show.upper()
print(f"Unique symbols used: {len(set(result_show))}")
print(result_show)




