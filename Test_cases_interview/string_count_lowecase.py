# find the frequence of letters in a given words:

letters = input("input letters of ur choice: ")
# eg: aabbbhggghjoisaaa
for i in range(97,123):
    count = 0
    j = chr(i)  # converting i to character value , unicode to character
    for l in letters.lower():
        if l == j:
            count += 1
    if count > 0:
        print(f'{j}{count}',end="")
        #print(j,":", count, end=" ")
