firstnum = int(input())
secondnum = int(input())
thirdnum = int(input())

largestnum = 0


if firstnum > secondnum and firstnum > thirdnum:
    largestnum = firstnum
elif secondnum > firstnum and secondnum > thirdnum:
    largestnum = secondnum
else:
    largestnum = thirdnum

print(largestnum)