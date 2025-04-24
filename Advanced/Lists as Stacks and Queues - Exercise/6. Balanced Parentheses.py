sequence = input()

while "()" in sequence or "{}" in sequence or "[]" in sequence:
    sequence = sequence.replace("()", "").replace("{}", "").replace("[]", "")

if not sequence:
    print("YES")
else:
    print("NO")