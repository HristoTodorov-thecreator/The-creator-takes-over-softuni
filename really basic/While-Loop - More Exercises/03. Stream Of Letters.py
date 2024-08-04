symbols =  ['A','a','B','b','D','d',"E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
           "L", "l", "M", "m", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w",
           "X", "x", "Y", "y", "Z", "z", "C", "N", "O"]


count_c = 0
count_n = 0
count_o = 0

result = ''
text = ''




while True:
    g = input()
    if g != 'End':


        if g == 'c':
            if count_c != 1:
                 count_c += 1
            else:
                 text += g
        elif g == 'o':
            if count_o != 1:
                 count_o += 1
            else:
                 text += g
        elif g == 'n':
            if count_n != 1:
                count_n += 1
            else:
                text += g

        else:
            if g in symbols:
                 text += g
            else:
                 continue

        if count_c + count_o + count_n == 3:
            result += text + ' '
            text = ''
            count_c = 0
            count_n = 0
            count_o = 0

    else:
       print(result)
       break


