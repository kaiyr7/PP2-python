def down(n):
    for i in range(n,0,-1):
        yield (i)
c=down(int(input()))
for i in c:
    print(i)