def spy_game(n):
    k=0
    for i in n:
        if(i==0 and k==0):
            k=1
        if(i==0 and k==1):
            k=2
        if(i==7 and k==2):
            k =3
        if(k==3):
            return True
    return False
l = []
n = int(input())
for i in range(n):
    a= int(input())
    l.append(a)
print(spy_game(l))