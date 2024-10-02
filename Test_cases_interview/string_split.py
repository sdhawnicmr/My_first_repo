# reverse every work in a given sentence:

sentence = input("enter the sentence u want to reverse: ")
new_sentence = sentence.split()
print(new_sentence)

for i in new_sentence:
    print(i[::-1], end=" ")

