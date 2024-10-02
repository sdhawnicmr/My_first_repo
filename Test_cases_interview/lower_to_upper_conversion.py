words = "abBcvhGSjJA"
upper = ""
A = 65
Z = 90
a = 97
z = 122
for i in words:
    # Check if the character is lowercase (between 'a' and 'z')
    if 'a' <= i <= 'z':
        upper += chr(ord(i) - 32)
    else:
        # If it's not a lowercase letter, add it as is
        upper += i

print(upper)  # Output: ABCVHGSJ






