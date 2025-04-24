
def s(*args):
    thetotal = 0
    second = 0

    for i in args:

        if i <0:
            thetotal += i

        elif i > 0:
            second += i

    return thetotal,second


g= [int(x) for x in input().split()]
negative, positive =(s(*g))

print(negative)
print(positive)



if abs(negative)< positive:
    print(f"The positives are stronger than the negatives")


else:
    print(f"The negatives are stronger than the positives")
