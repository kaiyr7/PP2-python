def truetuple():
    t = (0,1,2,3,False)
    for i in t:
        if(bool(i) == False):
            return False
    return True
print(truetuple())