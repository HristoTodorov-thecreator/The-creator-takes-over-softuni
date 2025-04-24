import math

x1 ,x2 = math.floor(float(input())),math.floor(float(input()))
y1,y2 = math.floor(float(input())),math.floor(float(input()))

to,tu = math.floor(float(input())),math.floor(float(input()))
po,pu = math.floor(float(input())),math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))
sum_t = math.floor(abs(to) + abs(tu))
sum_p = math.floor(abs(po) + abs(pu))

def t(ar1,ar2,ar3,ar4):
    one = ar1 + ar2
    two = ar3 + ar4
    if one > two:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"

    elif one <two:
        if abs(to) + abs(tu) > abs(po) + abs(pu):
            return f"({po}, {pu})({to}, {tu})"
        else:
            return f"({to}, {tu})({po}, {pu})"

    else:
        if abs(to) + abs(tu) > abs(po) + abs(pu):
            return f"({po}, {pu})({to}, {tu})"
        else:
            return f"({to}, {tu})({po}, {pu})"








print(t(sum_x,sum_y,sum_t,sum_p))
