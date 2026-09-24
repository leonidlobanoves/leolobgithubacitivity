def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.insert(len(lst), i)
    return lst