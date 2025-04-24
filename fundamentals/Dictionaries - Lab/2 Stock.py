first_input = input().split()

bakery = {}


for n in range(0,len(first_input),2):
    thekey = first_input[n]
    thevalue = first_input[n+1]
    bakery[thekey] = int(thevalue)


searched_products = input().split()

for i in searched_products:
    if i in bakery:
        print(f'We have {bakery[i]} of {i} left')

    else:
        print(f"Sorry, we don't have {i}")
