data = input()
saved_ = ""
bomb = 0

for i in range(len(data)):
    if data[i] == ">":
        bomb += int(data[i + 1])
        saved_ += data[i]
    elif data[i] != ">" and bomb > 0:
        bomb -= 1
    else:
        saved_ += data[i]

print(saved_)