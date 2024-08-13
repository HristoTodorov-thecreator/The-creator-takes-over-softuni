months = int(input())


water = 20
internet = 15
totalelect = 0
totalwater = water * months
totalinternet = internet * months
floth = 0

for i in range (months):
    others = 0
    electricity = float(input())
    totalelect += electricity
    others += water + internet + electricity
    floth += others + (others * 0.20)


total = totalwater + totalelect + totalinternet + floth
print(f"Electricity: {totalelect:.2f} lv")
print(f"Water: {totalwater:.2f} lv")
print(f"Internet: {totalinternet:.2f} lv")
print(f"Other: {floth:.2f} lv")
print(f"Average: {total / months:.2f} lv")