def reverseSentence(w):
    w=w.split(" ")
    l=list(w)
    l.reverse()
    for i in l:
        print(i, end = ' ')