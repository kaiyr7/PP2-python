s=str(input())
l=0
u=0
for i in s:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
print(l)
print(u)