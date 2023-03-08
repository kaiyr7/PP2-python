import os
os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
r=open("samp.txt",'r')
k=0
for line in r:
    k+=1
print(k)
r.close()