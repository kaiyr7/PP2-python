def div34(n):
    for i in n:
        if i%12==0:
            yield i
k=int(input())
a=div34([int(i) for i in range(k)])
for i in a:
    print(i)