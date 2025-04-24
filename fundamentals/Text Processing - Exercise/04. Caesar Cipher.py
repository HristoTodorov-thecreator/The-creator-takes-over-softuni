text = input()


secret_text = ""


for char in text:

    secret_text += chr(ord(char) + 3)


print(secret_text)