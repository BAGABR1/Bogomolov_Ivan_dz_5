def elem():
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    tmp = set()
    unq = set()
    for i in src:
        if i not in tmp:
            unq.add(i)
            tmp.add(i)
        else:
            unq.discard(i)
    src_unq = [i for i in src if i in unq]
    print(src_unq)


elem()
