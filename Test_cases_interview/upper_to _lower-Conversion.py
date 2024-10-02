words = input("enter strings: ")
lower = ""

for char in words:
    if 'A' <= char <= 'Z':
        lower += chr(ord(char)+32)
    else:
        lower += char
print(lower)