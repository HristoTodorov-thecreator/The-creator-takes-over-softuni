days = int(input())


reviewed = 0
unreviewed = 0
workers = 7
for i in range (1 ,days + 1):

    g = int(input())

    if i % 3 == 0:
        if unreviewed > reviewed:
            workers += 1



    if workers >= g:
        reviewed += g

    else:
        reviewed += workers
        unreviewed += g - workers


print(f"Treated patients: {reviewed}.")
print(f"Untreated patients: {unreviewed}.")


