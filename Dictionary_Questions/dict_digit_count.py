#calculate the sum of individual diguts
# if the digit count is repeating, calculate the sum of original digita
#compare the sum count and find the max digit

def sum_of_digits(n):
    sum_of_dig= 0
    while n > 0:
        dig = n % 10
        sum_of_dig += dig
        n= n//10
    return sum_of_dig

def sum_of_items(l):
    d = {}
    for n in l:
        sum_of_dig = sum_of_digits(n)
        if sum_of_dig not in d:
            d[sum_of_dig]=[]
        d[sum_of_dig].append(n)


    for k,v in d.items():
        v = sorted(v,reverse=True)
        d[k] = sum(v[:2])

    m =0
    for v in d.values():
        if v > m:
            m = v
    return m
l= [51,42,17,80,71]
sum_of_items(l)
