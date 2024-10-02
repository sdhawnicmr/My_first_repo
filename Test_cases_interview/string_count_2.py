# AABBBBBCCDEFGG : A2B5C2D1E1E1GG2

Letters = "AABBBBBCCDEFGGAG"
for i in range(65,91):
    j = chr(i)
    count = 0
    for l in Letters:
        if l == j:
            count+= 1
    if count > 0:
        print(f"{j}{count}",end="")
        #print(j,count, end="")