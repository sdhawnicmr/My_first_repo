# Remove duplicates
sentence = input("enter the sentence u want to reverse: ")
print(sentence)
duplicate_letters = ""
for i in sentence.lower():
    if i not in duplicate_letters:
        duplicate_letters += i

print(duplicate_letters)


