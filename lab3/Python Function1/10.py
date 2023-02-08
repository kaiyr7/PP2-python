def unique_list(x):
    l = []
    for i in x:
        if i not in l:
            l.append(i)
    return l