def filter_prime(list):
    v=[]
    for i in list:
        k=0
        if(i == 2):
            v.append(i)
            continue
        elif(i==1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                k+=1
        if(k==0):
            v.append(i)
    return v