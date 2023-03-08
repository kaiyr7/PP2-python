import os
os.chdir('/Users/Kaiyr/Documents/python/Lab1/lab6')
w=open("samp.txt",'w')
l=list(input().split())
for i in l:
    w.write(i.__str__()+" ")
w.close()