def recursive_sum(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    return l[0] + recursive_sum(l[1:])


l = [1, 2, 3, 4, 5, 6, 8]
print(recursive_sum(l))
