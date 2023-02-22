def square(a,b):
    for i in range(a,b):
        yield (i*i)
m=int(input())
n=int(input())
c=square(m,n)
for i in c:
    print(i)