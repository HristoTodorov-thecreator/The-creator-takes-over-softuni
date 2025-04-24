first = int(input())
second = int(input())
third = int(input())


listthe = []
listthe.append(first)
listthe.append(second)
listthe.append(third)


def smallestnum():
    g = min(listthe)
    return g

them = smallestnum()
print(them)
