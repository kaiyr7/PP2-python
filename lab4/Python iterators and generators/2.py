def evens(n):
    for i in n:
        if i%2==0:
            yield (i)
k=int(input())
a=evens([int(i) for i in range(k)])
for i in a:
    print(i,end=",")