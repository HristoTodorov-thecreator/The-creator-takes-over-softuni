wantedcm = int(input())
firstremovecm = wantedcm - 30
total = 0
counterfailed = 0

while firstremovecm <= wantedcm:
    jumps = int(input())

    if jumps <= firstremovecm:
        total += 1
        counterfailed += 1
    else:
        firstremovecm += 5
        total += 1
        counterfailed = 0

    if firstremovecm > wantedcm:
        print(f"Tihomir succeeded, he jumped over {firstremovecm - 5}cm after {total} jumps.")
        break
    if counterfailed == 3:
        print(f"Tihomir failed at {firstremovecm}cm after {total} jumps.")
        break






