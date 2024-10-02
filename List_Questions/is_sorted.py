lst = [4, 5, 6, 1, 9]


# could you pls check if the list is sorted ?
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


print(is_sorted(lst))



