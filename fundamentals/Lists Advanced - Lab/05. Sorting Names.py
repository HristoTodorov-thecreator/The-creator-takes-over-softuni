names_l = input().split(', ')

sorted_ = sorted(names_l,key= lambda x: (-len(x),x))

print(sorted_)